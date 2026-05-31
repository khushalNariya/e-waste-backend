from rest_framework import serializers
from django.contrib.auth.models import User
from app_14_reward_returns.Reward_Order_Return_Status_History__API__3.models import Reward_Order_Return_Status_History

# Serializer to show small user info (ID and Name)
class User_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]

# Main serializer for Return Status History
class Reward_Order_Return_Status_History_Serializer(serializers.ModelSerializer):
    user = User_Mini_Serializer(source="return_request.user", read_only=True)
    changed_by = User_Mini_Serializer(read_only=True)
    image = serializers.SerializerMethodField()
    return_number = serializers.CharField(source="return_request.return_number", read_only=True)

    # Custom date format (e.g., 17 Apr 2026, 11:20 PM)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True, source="created_at")

    class Meta:
        model = Reward_Order_Return_Status_History
        fields = [
            "id",
            "return_request",
            "return_number",
            "user",
            "image",
            "status",
            "remarks",
            "changed_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["return_request", "status", "changed_by"]

    # Function to get the absolute URL of the first return image proof
    def get_image(self, obj):
        request = self.context.get("request")
        first_image = obj.return_request.images.first()
        if first_image and first_image.image:
            return request.build_absolute_uri(first_image.image.url)
        return None
