from rest_framework import serializers
from django.utils import timezone
from django.db import transaction

# App 15 model imports
from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.models import Reward_Order_Replace_Request
from app_15_reward_replaces.Reward_Order_Replace_Items__API__2.models import Reward_Order_Replace_Item
from app_15_reward_replaces.Reward_Order_Replace_Status_History__API__3.models import Reward_Order_Replace_Status_History
from app_15_reward_replaces.Reward_Order_Replace_Pickups__API__4.models import Reward_Order_Replace_Pickup
from app_15_reward_replaces.Reward_Order_Replace_Images__API__5.models import Reward_Order_Replace_Image

# Other app model imports
from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order
from app_13_reward_orders.Reward_Order_Items__API__2.models import Reward_Order_Item
from app_13_reward_orders.Reward_Order_Address__API__3.models import Reward_Order_Address


# =============================================================
# MINI SERIALIZERS (Read-only nested representations)
# =============================================================

# Shows proof images inside replace request detail
class Replace_Image_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reward_Order_Replace_Image
        fields = ['id', 'image']


# Shows replaced items inside replace request detail
class Replace_Item_Mini_Serializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Reward_Order_Replace_Item
        fields = [
            'id',
            'order_item',
            'product',
            'product_name',
            'quantity',
            'points',
            'subtotal_points',
            'item_condition',
            'replacement_product',
            'replacement_product_name',
            'image',
        ]

    def get_image(self, obj):
        try:
            from app_9_Reward_Products.Reward_Product_Images__API__3.models import Reward_Product_Image_model
            img = Reward_Product_Image_model.objects.filter(product_id=obj.product_id, is_primary=True).first()
            if not img:
                img = Reward_Product_Image_model.objects.filter(product_id=obj.product_id).first()
            if img and img.image:
                request = self.context.get('request')
                if request:
                    return request.build_absolute_uri(img.image.url)
                return img.image.url
        except Exception:
            pass
        return None


# Shows pickup + tracking info inside replace request detail
class Replace_Pickup_Mini_Serializer(serializers.ModelSerializer):
    address_details = serializers.SerializerMethodField()

    class Meta:
        model = Reward_Order_Replace_Pickup
        fields = ['id', 'pickup_status', 'courier_name', 'tracking_number', 'address_details']

    def get_address_details(self, obj):
        addr = obj.order_address
        return {
            "full_name": addr.full_name,
            "phone":     addr.phone,
            "address":   addr.address,
            "city":      addr.city,
            "state":     addr.state,
            "pincode":   addr.pincode,
            "landmark":  addr.landmark,
        }


# =============================================================
# MAIN REPLACE REQUEST SERIALIZER
# Used by both Admin and User viewsets
# =============================================================
class Reward_Order_Replace_Request_Serializer(serializers.ModelSerializer):

    # Read-only computed fields for API output
    user_name    = serializers.SerializerMethodField()
    order_number = serializers.CharField(source='order.order_number', read_only=True)

    # Nested read-only sub-data
    images_data = Replace_Image_Mini_Serializer(source='images',  many=True, read_only=True)
    items_data  = Replace_Item_Mini_Serializer( source='items',   many=True, read_only=True)
    pickup_data = Replace_Pickup_Mini_Serializer(source='pickups', many=True, read_only=True)

    # Computed: timestamp when replacement was delivered (from status history)
    replacement_delivered_at = serializers.SerializerMethodField()
    # Cancellation audit info — populated only when status is 'rejected' by user
    cancel_info = serializers.SerializerMethodField()
    # Expected completion date (request date + 5 days)
    expected_by = serializers.SerializerMethodField()
    # Actual completion date from status history (when replacement_delivered)
    completed_at = serializers.SerializerMethodField()

    # Standard project date format
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    # Write-only: user selects order when submitting
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Reward_Order.objects.all(),
        source='order',
        write_only=True,
        error_messages={
            'required':      'Order selection is required.',
            'does_not_exist': 'Invalid order selected.',
        }
    )

    # Write-only: 1 to 5 proof photos required
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=True,
        error_messages={'required': 'At least 1 proof image is required.'}
    )

    # Write-only: list of items user wants to replace
    replace_items = serializers.JSONField(write_only=True, required=True)

    # Auto-inject logged-in user (hidden from input)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model  = Reward_Order_Replace_Request
        fields = [
            'id',
            'replace_number',
            'order_id',
            'order_number',
            'user',
            'user_name',
            'replace_status',
            'replace_reason',
            'replace_note',
            'replace_type',
            'replace_date',
            'replace_items',
            'images',
            'images_data',
            'items_data',
            'pickup_data',
            'replacement_delivered_at',
            'cancel_info',
            'expected_by',
            'completed_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['replace_number']

    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() or obj.user.username

    def get_expected_by(self, obj):
        """Returns expected completion date = request date + 5 days."""
        from datetime import timedelta
        expected = timezone.localtime(obj.created_at) + timedelta(days=5)
        return expected.strftime("%d %b %Y")

    def get_completed_at(self, obj):
        """Returns the date/time when replacement was delivered (terminal completion)."""
        history = obj.status_history.filter(status='replacement_delivered').order_by('-created_at').first()
        if history:
            return timezone.localtime(history.created_at).strftime("%d %b %Y, %I:%M %p")
        return None

    def get_cancel_info(self, obj):
        """Returns the rejection/cancellation log entry for user-cancelled requests."""
        if obj.replace_status != 'rejected':
            return None
        history = obj.status_history.filter(status='rejected').order_by('-created_at').first()
        if not history:
            return None
        # If rejected by admin/staff — show generic brand name, never expose internal names
        if history.changed_by and (history.changed_by.is_staff or history.changed_by.is_superuser):
            cancelled_by = "E-Waste Team"
        elif history.changed_by:
            full_name = f"{history.changed_by.first_name} {history.changed_by.last_name}".strip()
            cancelled_by = full_name or history.changed_by.username
        else:
            cancelled_by = "E-Waste Team"
        return {
            "cancelled_by": cancelled_by,
            "remarks": history.remarks,
            "cancelled_at": timezone.localtime(history.created_at).strftime("%d %b %Y, %I:%M %p"),
        }

    def get_replacement_delivered_at(self, obj):
        """
        Returns the ISO timestamp of when the replacement was delivered.
        Looks up the 'replacement_delivered' entry in the status history table.
        No DB schema change required — uses existing status history records.
        """
        history = obj.status_history.filter(status='replacement_delivered').order_by('-created_at').first()
        if history:
            return history.created_at.isoformat()
        return None

    # =============================================================
    # INPUT VALIDATION RULES
    # =============================================================

    def validate_images(self, images):
        # Must upload between 1 and 5 proof photos
        if len(images) < 1:
            raise serializers.ValidationError("At least 1 proof image is required.")
        if len(images) > 5:
            raise serializers.ValidationError("Maximum 5 proof images allowed.")
        return images

    def validate_replace_reason(self, value):
        # Reason must not be empty
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Replace reason cannot be empty.")
        return value

    def validate(self, data):
        # Run creation validations only (not on update)
        if not self.instance:
            user  = self.context['request'].user
            order = data.get('order')

            # Check order belongs to this user
            if order.user != user:
                raise serializers.ValidationError({"order_id": "You can only request replacement for your own orders."})

            # Check order is delivered
            if order.order_status != "delivered":
                raise serializers.ValidationError({"order_id": "Only delivered orders are eligible for replacement."})

            # Check 7-day replace window using delivered_at field
            if not order.delivered_at:
                raise serializers.ValidationError({"order_id": "Order delivery date is not recorded. Cannot process replacement."})

            days_since_delivery = (timezone.now() - order.delivered_at).days
            if days_since_delivery > 7:
                raise serializers.ValidationError({"order_id": f"Replace window has expired. Replacement is only allowed within 7 days of delivery. ({days_since_delivery} days have passed)"})

            # Validate each item in replace_items list
            replace_items = data.get('replace_items')
            if not isinstance(replace_items, list) or len(replace_items) == 0:
                raise serializers.ValidationError({"replace_items": "replace_items list is required and cannot be empty."})

            for idx, item in enumerate(replace_items):
                order_item_id = item.get('order_item_id')
                product_id    = item.get('product_id')
                qty           = item.get('quantity', 1)

                if not order_item_id or not product_id:
                    raise serializers.ValidationError({"replace_items": f"Item at index {idx} must have order_item_id and product_id."})

                # Verify item belongs to this order
                order_item = Reward_Order_Item.objects.filter(
                    id=order_item_id, order=order, product_id=product_id
                ).first()
                if not order_item:
                    raise serializers.ValidationError({"replace_items": f"Invalid item mapping for product_id {product_id} in this order."})

                from app_15_reward_replaces.Reward_Order_Replace_Items__API__2.models import Reward_Order_Replace_Item

                # -------------------------------------------------------
                # BLOCK RE-REPLACEMENT: If this item was already replaced
                # successfully (replacement_delivered), the user cannot replace it again — only return
                # within the replacement return window.
                # -------------------------------------------------------
                already_successfully_replaced = Reward_Order_Replace_Item.objects.filter(
                    order_item_id=order_item_id,
                    replace_request__order=order,
                    replace_request__replace_status__in=['replacement_delivered']
                ).exists()
                if already_successfully_replaced:
                    raise serializers.ValidationError({
                        "replace_items": (
                            f"Item at index {idx} has already been replaced once. "
                            "You can only return this item (within 1 day of replacement delivery). "
                            "Re-replacement is not allowed."
                        )
                    })

                # Calculate already replaced quantity for this order_item_id across non-rejected requests
                replaced_qtys = Reward_Order_Replace_Item.objects.filter(
                    replace_request__order=order,
                    order_item_id=order_item_id
                ).exclude(replace_request__replace_status='rejected').values_list('quantity', flat=True)

                # Calculate already returned quantity for this order_item_id across non-rejected requests
                from app_14_reward_returns.Reward_Order_Return_Items__API__2.models import Reward_Order_Return_Item
                returned_qtys = Reward_Order_Return_Item.objects.filter(
                    return_request__order=order,
                    order_item_id=order_item_id
                ).exclude(return_request__return_status='rejected').values_list('quantity', flat=True)
                
                total_replaced = sum(replaced_qtys)
                total_returned = sum(returned_qtys)
                remaining_qty = order_item.quantity - (total_replaced + total_returned)

                if qty <= 0 or qty != remaining_qty:
                    raise serializers.ValidationError({"replace_items": f"Invalid quantity {qty}. You must replace the full remaining quantity of {remaining_qty} for this item."})

        return data

    # =============================================================
    # STATUS SEQUENCE VALIDATOR (Admin Updates Only)
    # NOTE: Method MUST be named validate_replace_status because
    # DRF auto-calls validate_<fieldname> during validation.
    # =============================================================
    def validate_replace_status(self, value):
        # Only validate on update (when instance exists)
        if self.instance:
            current_status = self.instance.replace_status

            # Skip if status has not changed
            if value == current_status:
                return value

            new_status = value

            # Amazon-style linear replace flow.
            # NOTE: 'rejected' is NOT in this list — it is a special
            # exit state handled separately (can happen from any step).
            STATUS_FLOW = [
                'requested',
                'approved',
                'replacement_dispatched',
                'replacement_delivered',
            ]

            # Duplicate check (double safety — same as app_14)
            if new_status == current_status:
                raise serializers.ValidationError(
                    f"Status is already '{current_status}'. No change detected."
                )

            # Terminal state check — once replacement_delivered or rejected, no further change
            if current_status in ['rejected', 'replacement_delivered']:
                raise serializers.ValidationError(
                    f"Cannot change status. This replace request is already '{current_status}' (Terminal State)."
                )

            # 'rejected' is allowed from any non-terminal state (exit state)
            if new_status == 'rejected':
                return value

            # Sequence check — must follow the flow one step at a time
            try:
                if current_status not in STATUS_FLOW:
                    raise serializers.ValidationError(
                        f"Current status '{current_status}' cannot transition to '{new_status}'."
                    )

                current_idx = STATUS_FLOW.index(current_status)

                if new_status not in STATUS_FLOW:
                    raise serializers.ValidationError(f"'{new_status}' is not a valid status.")

                new_idx = STATUS_FLOW.index(new_status)

                # Only one step forward is allowed at a time
                if new_idx != current_idx + 1:
                    expected_next = STATUS_FLOW[current_idx + 1]
                    raise serializers.ValidationError(
                        f"Sequence Error! From '{current_status}', the only allowed next step is '{expected_next}'."
                    )

            except (ValueError, IndexError):
                raise serializers.ValidationError(
                    f"Invalid status transition from '{current_status}' to '{new_status}'."
                )

        return value

    # =============================================================
    # CREATE LOGIC (User submits replace request)
    # =============================================================
    @transaction.atomic
    def create(self, validated_data):
        user          = self.context['request'].user
        order         = validated_data.get('order')
        replace_items = validated_data.pop('replace_items', [])
        images        = validated_data.pop('images', [])

        # Step 1: Generate unique replace number using timestamp
        replace_number = "REP-" + timezone.now().strftime("%Y%m%d%H%M%S")
        validated_data['replace_number']  = replace_number
        validated_data['replace_status']  = 'requested'

        # Step 2: Loop items and prepare data to save
        items_to_save = []
        for item_data in replace_items:
            order_item = Reward_Order_Item.objects.get(
                id=item_data['order_item_id'],
                order=order
            )
            qty      = item_data.get('quantity', 1)
            subtotal = qty * order_item.points

            items_to_save.append({
                'order_item':                order_item,
                'product_id':               order_item.product_id,
                'product_name':             order_item.product_name,
                'quantity':                 qty,
                'points':                   order_item.points,
                'subtotal_points':          subtotal,
                'item_condition':           item_data.get('item_condition', 'wrong_item'),
                'replacement_product_id':   item_data.get('replacement_product_id', None),
                'replacement_product_name': item_data.get('replacement_product_name', None),
            })

        # Step 3: Save the main replace request
        replace_request = Reward_Order_Replace_Request.objects.create(**validated_data)

        # Step 4: Save each replace item
        for item in items_to_save:
            Reward_Order_Replace_Item.objects.create(
                replace_request=replace_request,
                order_item=item['order_item'],
                product_id=item['product_id'],
                product_name=item['product_name'],
                quantity=item['quantity'],
                points=item['points'],
                subtotal_points=item['subtotal_points'],
                item_condition=item['item_condition'],
                replacement_product_id=item['replacement_product_id'],
                replacement_product_name=item['replacement_product_name'],
            )

        # Step 5: Save proof images
        for img in images:
            Reward_Order_Replace_Image.objects.create(
                replace_request=replace_request,
                image=img
            )

        # Step 6: Write first status history log
        Reward_Order_Replace_Status_History.objects.create(
            replace_request=replace_request,
            status='requested',
            changed_by=user,
            remarks="Replace request submitted by user. Awaiting admin review."
        )

        # Step 7: Auto-create pickup record from delivery address
        order_address = Reward_Order_Address.objects.filter(order=order).first()
        if order_address:
            Reward_Order_Replace_Pickup.objects.create(
                replace_request=replace_request,
                order_address=order_address,
                pickup_status='scheduled',
                delivery_address=order_address,  # Same address for delivery of new item
            )

        return replace_request
