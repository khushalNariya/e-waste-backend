from rest_framework import serializers
from .models import Reward_Order_Return_Pickup

# Serializer for return courier pickup details - Read Only for Admin dashboard representation
class Reward_Order_Return_Pickup_Serializer(serializers.ModelSerializer):
    return_number = serializers.CharField(source='return_request.return_number', read_only=True)
    order_number = serializers.CharField(source='return_request.order.order_number', read_only=True)
    user_name = serializers.SerializerMethodField()
    address_details = serializers.SerializerMethodField()

    class Meta:
        model = Reward_Order_Return_Pickup
        fields = [
            'id',
            'return_request',
            'return_number',
            'order_number',
            'user_name',
            'order_address',
            'address_details',
            'pickup_status'
        ]

    def get_user_name(self, obj):
        user = obj.return_request.user
        return f"{user.first_name} {user.last_name}".strip() or user.username

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
