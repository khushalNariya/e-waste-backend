import re
from rest_framework import serializers
from django.utils import timezone
from django.db import transaction

# Model imports from returns app
from app_14_reward_returns.Reward_Order_Return_Request__API__1.models import Reward_Order_Return_Request
from app_14_reward_returns.Reward_Order_Return_Items__API__2.models import Reward_Order_Return_Item
from app_14_reward_returns.Reward_Order_Return_Status_History__API__3.models import Reward_Order_Return_Status_History
from app_14_reward_returns.Reward_Order_Return_Pickups__API__4.models import Reward_Order_Return_Pickup
from app_14_reward_returns.Reward_Order_Return_Images__API__5.models import Reward_Order_Return_Image

# Other project models
from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order
from app_13_reward_orders.Reward_Order_Items__API__2.models import Reward_Order_Item
from app_13_reward_orders.Reward_Order_Address__API__3.models import Reward_Order_Address
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model

# =========================================================
# 🔹 MINI SERIALIZERS (READ ONLY REPRESENTATIONS)
# =========================================================

# Serializer for proof images representation
class Return_Image_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reward_Order_Return_Image
        fields = ['id', 'image']

# Serializer for return items representation
class Return_Item_Mini_Serializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Reward_Order_Return_Item
        fields = [
            'id', 
            'order_item', 
            'product', 
            'product_name', 
            'quantity', 
            'points', 
            'subtotal_points', 
            'item_condition',
            'image'
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

# Serializer for courier pickup tracking representation
class Return_Pickup_Mini_Serializer(serializers.ModelSerializer):
    address_details = serializers.SerializerMethodField()

    class Meta:
        model = Reward_Order_Return_Pickup
        fields = ['id', 'pickup_status', 'address_details']

    def get_address_details(self, obj):
        addr = obj.order_address
        return {
            "full_name": addr.full_name,
            "phone": addr.phone,
            "address": addr.address,
            "city": addr.city,
            "state": addr.state,
            "pincode": addr.pincode,
            "landmark": addr.landmark
        }

# =========================================================
# 🔹 MAIN RETURN REQUEST SERIALIZER
# =========================================================
class Reward_Order_Return_Request_Serializer(serializers.ModelSerializer):
    # Read-only nested mappings for API output
    user_name = serializers.SerializerMethodField()
    order_number = serializers.CharField(source='order.order_number', read_only=True)
    images_data = Return_Image_Mini_Serializer(source='images', many=True, read_only=True)
    items_data = Return_Item_Mini_Serializer(source='items', many=True, read_only=True)
    pickup_data = Return_Pickup_Mini_Serializer(source='pickups', many=True, read_only=True)
    # Cancellation audit info — populated only when status is 'rejected' by user
    cancel_info = serializers.SerializerMethodField()
    # Expected completion date (request date + 5 days)
    expected_by = serializers.SerializerMethodField()
    # Actual completion date from status history (when status reached 'refunded')
    completed_at = serializers.SerializerMethodField()

    # Date formatting standard to the project
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    # Write-only input fields for user return submission
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Reward_Order.objects.all(),
        source='order',
        write_only=True,
        error_messages={
            'required': 'Order selection is required',
            'does_not_exist': 'Invalid order selected'
        }
    )
    
    # Custom image upload container (1 to 5 images allowed)
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=True,
        error_messages={'required': 'Proof images are required for return submission'}
    )

    # Nested items to return list
    return_items = serializers.JSONField(write_only=True, required=True)

    # Autoloop standard hidden user field
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reward_Order_Return_Request
        fields = [
            'id',
            'return_number',
            'order_id',
            'order_number',
            'user',
            'user_name',
            'return_status',
            'return_reason',
            'return_note',
            'refund_points',
            'return_date',
            'return_items',
            'images',
            'images_data',
            'items_data',
            'pickup_data',
            'cancel_info',
            'expected_by',
            'completed_at',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['return_number', 'refund_points']

    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() or obj.user.username

    def get_expected_by(self, obj):
        """Returns expected completion date = request date + 5 days."""
        from datetime import timedelta
        expected = timezone.localtime(obj.created_at) + timedelta(days=5)
        return expected.strftime("%d %b %Y")

    def get_completed_at(self, obj):
        """Returns the date/time when the request reached 'refunded' status."""
        history = obj.status_history.filter(status='refunded').order_by('-created_at').first()
        if history:
            return timezone.localtime(history.created_at).strftime("%d %b %Y, %I:%M %p")
        return None

    def get_cancel_info(self, obj):
        """Returns the rejection/cancellation log entry for user-cancelled requests."""
        if obj.return_status != 'rejected':
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

    # ==========================================
    # 🔹 INPUT VALIDATION RULES
    # ==========================================
    def validate_images(self, images):
        if len(images) < 1:
            raise serializers.ValidationError("At least 1 product image proof is required.")
        if len(images) > 5:
            raise serializers.ValidationError("You can upload a maximum of 5 proof images.")
        return images

    def validate_return_reason(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Return reason cannot be empty.")
        return value

    # Main Validation Handler
    def validate(self, data):
        # Validate order and user relation during creation
        if not self.instance:
            user = self.context['request'].user
            order = data.get('order')

            if order.user != user:
                raise serializers.ValidationError({"order_id": "You can only request returns for your own orders."})

            # Check if the order was actually delivered
            if order.order_status != "delivered":
                raise serializers.ValidationError({"order_id": "Only delivered orders can be requested for returns."})

            # Parse and validate returned products listing
            return_items = data.get('return_items')
            if not isinstance(return_items, list) or len(return_items) == 0:
                raise serializers.ValidationError({"return_items": "return_items list is required and cannot be empty."})

            # Check original 1-day window (order delivered_at)
            original_window_open = False
            if order.delivered_at:
                from django.utils import timezone as tz
                d1 = order.delivered_at.replace(hour=0, minute=0, second=0, microsecond=0)
                d2 = tz.now().replace(hour=0, minute=0, second=0, microsecond=0)
                diff = (d2 - d1).days
                original_window_open = diff <= 1

            for idx, item in enumerate(return_items):
                order_item_id = item.get('order_item_id')
                product_id = item.get('product_id')
                qty = item.get('quantity', 1)

                if not order_item_id or not product_id:
                    raise serializers.ValidationError({"return_items": f"Item at index {idx} must contain order_item_id and product_id."})

                # Retrieve order item details from order
                order_item = Reward_Order_Item.objects.filter(id=order_item_id, order=order, product_id=product_id).first()
                if not order_item:
                    raise serializers.ValidationError({"return_items": f"Invalid order item mapping for product id {product_id} inside this order."})

                # -----------------------------------------------------------
                # REPLACEMENT WINDOW CHECK
                # If original window is closed, check if this item has an
                # active replacement that was delivered within the last 1 day.
                # If yes, allow the return (replacement return window).
                # -----------------------------------------------------------
                from app_15_reward_replaces.Reward_Order_Replace_Items__API__2.models import Reward_Order_Replace_Item
                from app_15_reward_replaces.Reward_Order_Replace_Status_History__API__3.models import Reward_Order_Replace_Status_History

                replacement_window_open = False
                # Find completed replacement requests for this specific order item
                replace_item = Reward_Order_Replace_Item.objects.filter(
                    order_item_id=order_item_id,
                    replace_request__order=order,
                    replace_request__replace_status__in=['replacement_delivered']
                ).exclude(replace_request__replace_status='rejected').order_by('-id').first()

                if replace_item:
                    # Get timestamp when replacement_delivered status was set
                    rep_history = Reward_Order_Replace_Status_History.objects.filter(
                        replace_request=replace_item.replace_request,
                        status='replacement_delivered'
                    ).order_by('-created_at').first()

                    if rep_history:
                        from django.utils import timezone as tz
                        rd1 = rep_history.created_at.replace(hour=0, minute=0, second=0, microsecond=0)
                        rd2 = tz.now().replace(hour=0, minute=0, second=0, microsecond=0)
                        rep_diff = (rd2 - rd1).days
                        replacement_window_open = rep_diff <= 1

                # If neither window is open, block the return
                if not original_window_open and not replacement_window_open:
                    raise serializers.ValidationError({"order_id": "Return/replace window has expired for this order. Returns are only allowed within 1 day of delivery or 1 day of replacement delivery."})

                # Calculate already returned quantity for this order_item_id across non-rejected requests
                from app_14_reward_returns.Reward_Order_Return_Items__API__2.models import Reward_Order_Return_Item
                returned_qtys = Reward_Order_Return_Item.objects.filter(
                    return_request__order=order,
                    order_item_id=order_item_id
                ).exclude(return_request__return_status='rejected').values_list('quantity', flat=True)
                
                # Calculate already replaced quantity for this order_item_id across non-rejected requests
                replaced_qtys = Reward_Order_Replace_Item.objects.filter(
                    replace_request__order=order,
                    order_item_id=order_item_id
                ).exclude(replace_request__replace_status='rejected').values_list('quantity', flat=True)
                
                total_returned = sum(returned_qtys)
                total_replaced = sum(replaced_qtys)
                
                if original_window_open and replacement_window_open:
                    remaining_qty = order_item.quantity - total_returned
                elif original_window_open and not replacement_window_open:
                    remaining_qty = order_item.quantity - (total_returned + total_replaced)
                elif not original_window_open and replacement_window_open:
                    remaining_qty = total_replaced - total_returned
                else:
                    remaining_qty = 0

                if qty <= 0 or qty != remaining_qty:
                    raise serializers.ValidationError({"return_items": f"Invalid quantity {qty} requested. You must return the full remaining quantity of {remaining_qty} for this item."})

        return data

    # ==========================================
    # 🔹 STATUS SEQUENCING VALIDATOR (ADMIN UPDATES)
    # ==========================================
    # NOTE: Method name MUST be validate_return_status because the field is named 'return_status'.
    # DRF automatically calls validate_<fieldname> during validation.
    def validate_return_status(self, value):
        # We only validate during UPDATE (when instance exists)
        if self.instance:
            current_status = self.instance.return_status

            # Step 1: Skip validation if status is not changed (same as app_10)
            if value == current_status:
                return value

            new_status = value

            # Standard linear workflow sequence
            # NOTE: 'rejected' is NOT included here because it is a special exit state
            # that can be applied from any non-terminal status (handled separately below)
            STATUS_FLOW = [
                'requested',
                'approved',
                'pickup_scheduled',
                'picked_up',
                'received',
                'inspected',
                'refund_approved',
                'refunded'
            ]

            # Step 2: Duplicate check (double safety net, same as app_10)
            if new_status == current_status:
                raise serializers.ValidationError(
                    f"Status is already set to '{current_status}'. No change detected."
                )

            # Step 3: Terminal State check — Once rejected or refunded, no further changes allowed
            if current_status in ['rejected', 'refunded']:
                raise serializers.ValidationError(
                    f"Cannot change status. This return request is already '{current_status}' (Terminal State)."
                )

            # Step 4: Special exit — 'rejected' is allowed from any non-terminal state
            if new_status == 'rejected':
                return value

            # Step 5: Sequence check for standard flow (same as app_10)
            try:
                # If current status is not in the standard flow, block the transition
                if current_status not in STATUS_FLOW:
                    raise serializers.ValidationError(
                        f"Current status '{current_status}' cannot transition to '{new_status}'."
                    )

                current_idx = STATUS_FLOW.index(current_status)

                # If new status is also not in the flow, block the transition
                if new_status not in STATUS_FLOW:
                    raise serializers.ValidationError(f"'{new_status}' is not a valid status name.")

                new_idx = STATUS_FLOW.index(new_status)

                # Enforce strictly one-step-at-a-time transition (same as app_10)
                if new_idx != current_idx + 1:
                    expected_next = STATUS_FLOW[current_idx + 1]
                    raise serializers.ValidationError(
                        f"Sequence Error! From '{current_status}', the only allowed next step is '{expected_next}'."
                    )
            except (ValueError, IndexError):
                raise serializers.ValidationError(
                    f"Invalid status transition logic from '{current_status}' to '{new_status}'."
                )

        return value

    # ==========================================
    # 🔹 CREATE LOGIC (FOR USERS)
    # ==========================================
    @transaction.atomic
    def create(self, validated_data):
        user = self.context['request'].user
        order = validated_data.get('order')
        return_items = validated_data.pop('return_items', [])
        images = validated_data.pop('images', [])

        # Step 1: Create unique return number
        return_number = "RET-" + timezone.now().strftime("%Y%m%d%H%M%S")
        validated_data['return_number'] = return_number
        validated_data['return_status'] = 'requested'

        # Step 2: Loop items and calculate points
        total_refund_points = 0
        items_to_save = []

        for item_data in return_items:
            order_item = Reward_Order_Item.objects.get(
                id=item_data['order_item_id'], 
                order=order
            )
            qty = item_data.get('quantity', 1)
            subtotal = qty * order_item.points
            total_refund_points += subtotal

            items_to_save.append({
                'order_item': order_item,
                'product_id': order_item.product_id,
                'product_name': order_item.product_name,
                'quantity': qty,
                'points': order_item.points,
                'subtotal_points': subtotal,
                'item_condition': item_data.get('item_condition', 'wrong_item')
            })

        validated_data['refund_points'] = total_refund_points

        # Step 3: Save Return Request
        return_request = Reward_Order_Return_Request.objects.create(**validated_data)

        # Step 4: Save Return Items
        for item in items_to_save:
            Reward_Order_Return_Item.objects.create(
                return_request=return_request,
                order_item=item['order_item'],
                product_id=item['product_id'],
                product_name=item['product_name'],
                quantity=item['quantity'],
                points=item['points'],
                subtotal_points=item['subtotal_points'],
                item_condition=item['item_condition']
            )

        # Step 5: Save Proof Images
        for img in images:
            Reward_Order_Return_Image.objects.create(
                return_request=return_request,
                image=img
            )

        # Step 6: Create Automatic Status History log
        Reward_Order_Return_Status_History.objects.create(
            return_request=return_request,
            status='requested',
            changed_by=user,
            remarks="Return request registered successfully by user. Awaiting admin approval."
        )

        # Step 7: Create Automatic Return Pickup Scheduler record
        order_address = Reward_Order_Address.objects.filter(order=order).first()
        if order_address:
            Reward_Order_Return_Pickup.objects.create(
                return_request=return_request,
                order_address=order_address,
                pickup_status='scheduled'
            )

        return return_request
