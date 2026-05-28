from rest_framework import serializers
from .models import Reward_Order_Status_History
from django.contrib.auth.models import User


class User_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class Reward_Order_Status_History_Serializer(serializers.ModelSerializer):
    order_number = serializers.CharField(source="order.order_number", read_only=True)
    user_name = serializers.SerializerMethodField()
    changed_by = User_Mini_Serializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    class Meta:
        model = Reward_Order_Status_History
        fields = [
            "id",
            "order",
            "order_number",
            "user_name",
            "status",
            "remarks",
            "changed_by",
            "created_at",
            "updated_at",
        ]

    def get_user_name(self, obj):
        if obj.order and obj.order.user:
            return f"{obj.order.user.first_name} {obj.order.user.last_name}"
        return "Unknown"
