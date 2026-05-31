from rest_framework import serializers
from app_8_Reward_Rules.models import Reward_Rule_model, Item_Condition_model
from app_3_Recycling_info.models import Recycle_Category


# ===============================
# 🔹 MINI SERIALIZERS
# ===============================


class CategoryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recycle_Category
        fields = ["id", "title"]  # 👈 only required


class ConditionMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Condition_model
        fields = ["id", "display_name"]  # 👈 UI friendly


# ===============================
# 🔹 MAIN SERIALIZER
# ===============================


class Reward_Rule_Serializer(serializers.ModelSerializer):

    # ✅ READ (GET → full object)
    category = CategoryMiniSerializer(read_only=True)
    condition = ConditionMiniSerializer(read_only=True)

    # ✅ WRITE (POST/PUT → id pass)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Recycle_Category.objects.all(),
        source="category",
        write_only=True,
        error_messages={
            "required": "Please select category",
            "null": "Please select category",
            "does_not_exist": "Invalid category",
            "incorrect_type": "Invalid category id",
        },
    )

    condition_id = serializers.PrimaryKeyRelatedField(
        queryset=Item_Condition_model.objects.all(),
        source="condition",
        write_only=True,
        error_messages={
            "required": "Please select condition",
            "null": "Please select condition",
            "does_not_exist": "Invalid condition",
            "incorrect_type": "Invalid condition id",
        },
    )

    points = serializers.IntegerField(
        required=True,
        min_value=1,
        error_messages={
            "required": "Points is required",
            "invalid": "Points must be a number",
            "null": "Points cannot be empty",
            "min_value": "Points must be greater than 0",
        },
    )
    unit = serializers.ChoiceField(
        choices=Reward_Rule_model.UNIT_CHOICES,
        error_messages={
            "required": "Please select unit",
            "null": "Please select unit",
            "invalid_choice": "please select valid unit",
        },
    )

    # ✅ DATE FORMAT
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    # ✅ OPTIONAL FIELD
    is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Reward_Rule_model
        fields = [
            "id",
            "category",
            "condition",
            "category_id",
            "condition_id",
            "points",
            "unit",
            "is_active",
            "created_at",
            "updated_at",
        ]

    def validate(self, data):
        category = data.get("category")
        condition = data.get("condition")

        qs = Reward_Rule_model.objects.filter(category=category, condition=condition)

        # edit case ignore current id
        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError({"non_field_errors": ["Already exists"]})

        return data
