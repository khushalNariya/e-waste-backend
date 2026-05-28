from rest_framework import serializers
from django.contrib.auth.models import User
from app_15_reward_replaces.Reward_Order_Replace_Status_History__API__3.models import Reward_Order_Replace_Status_History


# Small user info for changed_by field display
class User_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ["id", "first_name", "last_name"]


# Main serializer for replace status history — read-only audit log
class Reward_Order_Replace_Status_History_Serializer(serializers.ModelSerializer):
    user         = User_Mini_Serializer(source="replace_request.user", read_only=True)
    changed_by   = User_Mini_Serializer(read_only=True)
    replace_number = serializers.CharField(source="replace_request.replace_number", read_only=True)
    image        = serializers.SerializerMethodField()

    # Standard project date format
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True, source="created_at")

    class Meta:
        model  = Reward_Order_Replace_Status_History
        fields = [
            "id",
            "replace_request",
            "replace_number",
            "user",
            "image",
            "status",
            "remarks",
            "changed_by",
            "created_at",
            "updated_at",
        ]
        # Status and changed_by are written by system only — not editable via API
        read_only_fields = ["replace_request", "status", "changed_by"]

    # Returns URL of the first proof image uploaded by user
    def get_image(self, obj):
        request     = self.context.get("request")
        first_image = obj.replace_request.images.first()
        if first_image and first_image.image:
            return request.build_absolute_uri(first_image.image.url)
        return None
