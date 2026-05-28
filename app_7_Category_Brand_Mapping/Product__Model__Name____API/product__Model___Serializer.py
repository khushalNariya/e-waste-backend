from rest_framework import serializers
from app_7_Category_Brand_Mapping.models import Product_Model_Name_Model
from app_3_Recycling_info.models import Recycle_Category
from app_6_Brands.models import Brand


# MINI serializers
class CategoryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recycle_Category
        fields = ["id", "title"]


class BrandMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]


class Product_Model_Name_Serializer(serializers.ModelSerializer):

    # READ
    category = CategoryMiniSerializer(read_only=True)
    brand = BrandMiniSerializer(read_only=True)

    # # WRITE
    # category_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Recycle_Category.objects.all(), source="category", write_only=True
    # )

    # brand_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Brand.objects.all(), source="brand", write_only=True
    # )

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

    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(),
        source="brand",
        write_only=True,
        error_messages={
            "required": "Please select brand",
            "null": "Please select brand",
            "does_not_exist": "Invalid brand",
            "incorrect_type": "Invalid brand id",
        },
    )

    model_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Model name is required",
            "blank": "Model name cannot be empty",
            
        },
    )

    # ✅ DATE FORMAT (optional but good)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Product_Model_Name_Model
        fields = [
            "id",
            "category",
            "brand",
            "category_id",
            "brand_id",
            "model_name",
            "is_active",
            "created_at",
            "updated_at",
        ]

    # ====================== Duplicate validation ======================

    def validate(self, data):
        """
        1. Trim all fields (remove spaces)
        2. Check duplicate
        """

        # 🔥 STEP 1: TRIM ALL STRING FIELDS
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()


        # 🔥 STEP 2: DUPLICATE CHECK
        category = data.get("category")
        brand = data.get("brand")
        model_name = data.get("model_name", "").strip()

        qs = Product_Model_Name_Model.objects.filter(
            category=category, brand=brand, model_name__iexact=model_name
        )

        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError(
                {"non_field_errors": ["Model already exists for this brand"]}
            )

        return data

    # def validate(self, data):
    #     category = data.get("category")
    #     brand = data.get("brand")
    #     model_name = data.get("model_name")

    #     qs = Product_Model_Name_Model.objects.filter(
    #         category=category, brand=brand, model_name__iexact=model_name
    #     )

    #     if self.instance:
    #         qs = qs.exclude(id=self.instance.id)

    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             {"non_field_errors": ["Model Name already exists for this Category and Brand"]}
    #         )

    #     return data
