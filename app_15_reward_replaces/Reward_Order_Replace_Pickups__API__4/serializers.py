from rest_framework import serializers
from app_15_reward_replaces.Reward_Order_Replace_Pickups__API__4.models import Reward_Order_Replace_Pickup


# Serializer for replace pickup + delivery tracking — read-only for admin
class Reward_Order_Replace_Pickup_Serializer(serializers.ModelSerializer):
    replace_number = serializers.CharField(source='replace_request.replace_number', read_only=True)
    order_number   = serializers.CharField(source='replace_request.order.order_number', read_only=True)
    user_name      = serializers.SerializerMethodField()
    address_details = serializers.SerializerMethodField()

    class Meta:
        model  = Reward_Order_Replace_Pickup
        fields = [
            'id',
            'replace_request',
            'replace_number',
            'order_number',
            'user_name',
            'order_address',
            'address_details',
            'pickup_status',
            'courier_name',
            'tracking_number',
        ]

    def get_user_name(self, obj):
        user = obj.replace_request.user
        return f"{user.first_name} {user.last_name}".strip() or user.username

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
