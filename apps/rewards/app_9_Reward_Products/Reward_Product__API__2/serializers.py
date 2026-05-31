from rest_framework import serializers

# import serializer (Reward_Product_Image_Serializer) API --- 3
from app_9_Reward_Products.Reward_Product_Images__API__3.serializers import (
    Reward_Product_Image_Serializer,
)

# import Model
from .models import Reward_Product_model

# import Model (Reward_Category_model) API --- 1
from app_9_Reward_Products.Reward_Category__API__1.models import Reward_Category_model


# ===============================
# 🔹 MINI SERIALIZERS (ONLY FOR MAPPING)
# ===============================


class RewardCategoryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward_Category_model
        fields = ["id", "name"]  # 👈 only required


# ===============================
# 🔹 MAIN REWARD PRODUCT SERIALIZER
# ===============================


class Reward_Product_Serializer(serializers.ModelSerializer):

    # ✅ READ (GET → {} format with name)
    category = RewardCategoryMiniSerializer(read_only=True)

    # ✅ WRITE (POST → id pass karo)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Reward_Category_model.objects.all(), source="category", write_only=True
    )

    # Nested images (Only active ones)
    images = serializers.SerializerMethodField()

    # DATE FORMAT
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    # ================= FIELD VALIDATION =================

    terms = serializers.CharField(required=False, allow_blank=True)
    tag = serializers.CharField(required=False, allow_blank=True)
    delivery_days = serializers.CharField(required=False, allow_blank=True)

    name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Product name is required",
            "blank": "Product name cannot be empty",
        },
    )

    points = serializers.IntegerField(
        required=True,
        min_value=0,
        error_messages={
            "required": "Reward points are required",
            "min_value": "Points cannot be negative",
            "invalid": "Points must be a valid number",
        },
    )

    stock = serializers.IntegerField(
        required=True,
        min_value=0,
        error_messages={
            "required": "Stock count is required",
            "min_value": "Stock cannot be negative",
            "invalid": "Stock must be a valid number",
        },
    )

    description = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Description is required",
            "blank": "Description cannot be empty",
        },
    )

    is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Reward_Product_model
        fields = [
            "id",
            "category",
            "category_id",
            "name",
            "slug",
            "points",
            "stock",
            "description",
            "terms",
            "tag",
            "delivery_days",
            "rating",
            "total_redeemed",
            "is_active",
            "created_at",
            "updated_at",
            "images",
        ]
        read_only_fields = ["slug"]

    # ✅ COMMON VALIDATION
    def validate(self, data):
        # TRIM ALL STRING FIELDS
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        name = data.get("name")
        category = data.get("category")

        # If name or category is not provided (e.g. during partial update), skip comparison
        if name and category:
            qs = Reward_Product_model.objects.filter(
                name__iexact=name, category=category
            )

            if self.instance:
                qs = qs.exclude(id=self.instance.id)

            if qs.exists():
                raise serializers.ValidationError(
                    {"name": ["This product already exists in this category"]}
                )

        return data

    def get_images(self, obj):
        # Only serialize active images for the product
        active_images = obj.images.filter(is_active=True).order_by('display_order')
        return Reward_Product_Image_Serializer(active_images, many=True, context=self.context).data
