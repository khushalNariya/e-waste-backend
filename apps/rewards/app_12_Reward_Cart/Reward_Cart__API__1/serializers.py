from rest_framework import serializers   
from .models import (
    Reward_Cart_Model
)

from app_12_Reward_Cart.Reward_Cart_Items__API__2.serializers import Reward_Cart_Items_Serializer





# ============================================================
# CART SERIALIZER
# ============================================================

class Reward_Cart_Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    
    cart_items = Reward_Cart_Items_Serializer(
        many=True,
        read_only=True
    )

    user_name = serializers.SerializerMethodField()

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    class Meta:

        model = Reward_Cart_Model

        fields = [
            "id",
            "user",
            "user_name",
            "email",
            "status",
            "total_points",
            "cart_items",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "user",
            "total_points",
        ]

    def get_user_name(self, obj):

        return f"{obj.user.first_name} {obj.user.last_name}"