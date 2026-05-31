from rest_framework import serializers
from app_7_Category_Brand_Mapping.models import Category_Brand_Mapping_Model

from app_3_Recycling_info.models import Recycle_Category
from app_6_Brands.models import Brand

# ===============================
# 🔹 MINI SERIALIZERS (ONLY FOR MAPPING)
# ===============================


class CategoryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recycle_Category
        fields = ["id", "title"]  # 👈 only required


class BrandMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]  # 👈 only required


# ===============================
# 🔹 MAIN MAPPING SERIALIZER
# ===============================


class Category_Brand_Mapping_Serializer(serializers.ModelSerializer):

    # ✅ READ (GET → {} format with name)
    category = CategoryMiniSerializer(read_only=True)
    brand = BrandMiniSerializer(read_only=True)

    # ✅ WRITE (POST → id pass karo)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Recycle_Category.objects.all(), source="category", write_only=True
    )

    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), source="brand", write_only=True
    )

    # ✅ DATE FORMAT (optional but good)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Category_Brand_Mapping_Model
        fields = [
            "id",
            "category",
            "brand",
            "category_id",
            "brand_id",
            "is_active",
            "created_at",
            "updated_at",
        ]

    # ✅ VALIDATION (duplicate prevent)
    # def validate(self, data):
    #     category = data.get('category')
    #     brand = data.get('brand')

    #     if Category_Brand_Mapping_Model.objects.filter(category=category, brand=brand).exists():
    #         raise serializers.ValidationError("This brand already exists in this category")

    #     return data

    def validate(self, data):
        category = data.get("category")
        brand = data.get("brand")

        qs = Category_Brand_Mapping_Model.objects.filter(category=category, brand=brand)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError(
                {"non_field_errors": ["This brand already exists in this category"]}
            )

        return data
