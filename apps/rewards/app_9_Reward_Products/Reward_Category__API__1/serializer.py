# app_rewards/serializers.py

from rest_framework import serializers
from .models import Reward_Category_model

class Reward_Category_Serializer(serializers.ModelSerializer):

    # DATE FORMAT (optional but good)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)


    name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Reward Category name is required",
            "blank": "Reward Category name cannot be empty",
            
        },
    )
    class Meta:
        model = Reward_Category_model
        fields = "__all__"
        read_only_fields =['slug']


     # ================= COMMON VALIDATION =================
    def validate(self, data):
        """
        Step 1: Trim all string fields (remove spaces)
        """

        # TRIM ALL FIELDS
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        return data

    # ================= VALIDATION =================

    def validate_name(self, value):
        """
        Prevent duplicate category name (case-insensitive)
        """
        value = value.strip()

        qs = Reward_Category_model.objects.filter(name__iexact=value)

        # Exclude current record during update
        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError("Category already exists")

        return value