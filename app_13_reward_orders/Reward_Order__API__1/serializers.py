from rest_framework import serializers
from .models import Reward_Order
from app_13_reward_orders.Reward_Order_Items__API__2.serializers import Reward_Order_Item_Serializer
from app_13_reward_orders.Reward_Order_Address__API__3.serializers import Reward_Order_Address_Serializer

# ==========================================
# ORDER SERIALIZER
# ==========================================
class Reward_Order_Serializer(serializers.ModelSerializer):
    items = Reward_Order_Item_Serializer(many=True, read_only=True)
    address = Reward_Order_Address_Serializer(read_only=True)
    status_history = serializers.SerializerMethodField()
    
    user_name = serializers.SerializerMethodField()
    email = serializers.EmailField(source="user.email", read_only=True)
    
    payment_status = serializers.SerializerMethodField()
    admin_notes = serializers.SerializerMethodField()
    
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    delivered_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True, allow_null=True)

    class Meta:
        model = Reward_Order
        fields = [
            "id",
            "order_number",
            "user",
            "user_name",
            "email",
            "cart_id",
            "total_points",
            "order_status",
            "payment_status",
            "admin_notes",
            "status_history",
            "items",
            "address",
            "delivered_at",
            "created_at",
            "updated_at",
        ]

    def get_status_history(self, obj):
        from app_13_reward_orders.Reward_Order_Status_History__API__5.serializers import Reward_Order_Status_History_Serializer
        history = obj.status_history.all().order_by("id")
        return Reward_Order_Status_History_Serializer(history, many=True).data

    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def get_payment_status(self, obj):
        try:
            return obj.payment.payment_status
        except:
            return "N/A"

    def get_admin_notes(self, obj):
        if obj.order_status == "cancelled":
            from app_13_reward_orders.Reward_Order_Status_History__API__5.models import Reward_Order_Status_History
            history = Reward_Order_Status_History.objects.filter(order=obj, status="cancelled").last()
            if history and history.changed_by.is_staff:
                return "Order was cancelled by the administrator. Your points have been refunded to your eco-wallet."
        return None

    # =====================================================
    # Method to automatically set payment_status to "paid" when order_status becomes "processing"
    # =====================================================
    # =============================================================
    # 🔥 STATUS FLOW & VALIDATION LOGIC (Sequencing)
    # =============================================================
    def validate_order_status(self, value):
        # We only validate during UPDATE (when instance exists)
        if self.instance:
            current_status = self.instance.order_status

            # 1. ✅ DUPLICATE CHECK
            if value == current_status:
                return value

            new_status = value

            # 2. ⛔ TERMINAL STATE CHECK
            if current_status in ["delivered", "cancelled", "returned", "failed"]:
                raise serializers.ValidationError(
                    f"Cannot change status. This order is already '{current_status}' (Terminal State)."
                )

            # Standard linear flow
            STATUS_FLOW = [
                "pending",
                "confirmed",
                "processing",
                "packed",
                "shipped",
                "out_for_delivery",
                "delivered"
            ]

            # 3. ⚠️ SPECIAL CASES (Exceptions)
            if new_status in ["cancelled", "failed", "returned"]:
                return value

            # 4. 📈 SEQUENCE CHECK (Step-by-Step)
            try:
                if current_status in STATUS_FLOW and new_status in STATUS_FLOW:
                    current_index = STATUS_FLOW.index(current_status)
                    new_index = STATUS_FLOW.index(new_status)

                    # Enforce strictly one-step-at-a-time transition
                    if new_index != current_index + 1:
                        expected_next = STATUS_FLOW[current_index + 1]
                        raise serializers.ValidationError(
                            f"Invalid Sequence! From '{current_status}', the only allowed next step is '{expected_next}'."
                        )
                else:
                    # If current status isn't in standard flow
                    if new_status in STATUS_FLOW:
                        raise serializers.ValidationError(
                            f"Current status '{current_status}' cannot transition to '{new_status}'."
                        )
            except (ValueError, IndexError):
                raise serializers.ValidationError(
                    f"Invalid status transition logic from '{current_status}' to '{new_status}'."
                )

        return value

    def validate(self, attrs):
        return attrs

