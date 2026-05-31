from rest_framework import serializers
from app_8_Reward_Rules.models import Item_Condition_model


from rest_framework import serializers

# from .models import Brand, CategoryBrandMapping

# Brand Serializer


class Item_Condition_Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    # ================= FIELD VALIDATION =================

    name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Name cannot be empty",
            "blank": "Name cannot be empty",
        },
    )

    display_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Display name is required",
            "blank": "Display name cannot be empty",
        },
    )

    is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Item_Condition_model
        fields = ["id", "name", "display_name", "is_active", "created_at", "updated_at"]

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

    # =========================== Duplicate (Check) ==============================
    def validate_name(self, value):
        value = value.strip()  # normalize

        qs = Item_Condition_model.objects.filter(name=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError("Condition already exists")

        return value

    # ✅ display_name (OPTIONAL strict)
    def validate_display_name(self, value):
        value = value.strip()

        qs = Item_Condition_model.objects.filter(display_name=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError("Display name already exists")

        return value

    # def validate_name(self, value):
    #     instance = self.instance

    #     # check duplicate (except current record)
    #     if ItemCondition.objects.filter(name=value).exclude(id=instance.id if instance else None).exists():
    #         raise serializers.ValidationError("This condition already exists.")

    #     return value
