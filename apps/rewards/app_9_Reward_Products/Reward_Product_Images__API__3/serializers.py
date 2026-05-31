# serializers.py

from rest_framework import serializers
from .models import Reward_Product_model, Reward_Product_Image_model, product_image_upload_path
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model
import os
from django.conf import settings
from .order_logic__CREATE__UPDATE import handle_create_order, handle_update_order, handle_product_change_order, move_image

# ===============================
# 🔹 MINI SERIALIZERS (ONLY FOR MAPPING)
# ===============================

class Reward_Product_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reward_Product_model
        fields = ["id", "name"]

# ===============================
# 🔹 MAIN MAPPING SERIALIZER
# ===============================

class Reward_Product_Image_Serializer(serializers.ModelSerializer):

    # ✅ READ
    product = Reward_Product_Mini_Serializer(read_only=True)

    # ✅ WRITE
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Reward_Product_model.objects.all(), source="product", write_only=True
    )

    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    class Meta:
        model = Reward_Product_Image_model
        fields = [
            "id", "product", "product_id", "image", 
            "is_primary", "display_order", "is_active", 
            "created_at", "updated_at",
        ]
        validators = [] # Disable unique together for swap logic

    image = serializers.ImageField(required=True)
    is_primary = serializers.BooleanField(required=True)
    display_order = serializers.IntegerField(required=False, allow_null=True)
    is_active = serializers.BooleanField(required=False, default=True)

    def validate(self, data):
        # TRIM ALL FIELDS
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        if not self.instance and not data.get("image"):
            raise serializers.ValidationError({"image": "Image is required."})
        return data

    # ================= CREATE =================
    def create(self, validated_data):
        product = validated_data["product"]
        display_order = validated_data.get("display_order")
        is_primary = validated_data.get("is_primary", False)

        # ✅ PRIMARY LOGIC
        if is_primary:
            Reward_Product_Image_model.objects.filter(product=product).update(is_primary=False)

        validated_data["display_order"] = handle_create_order(product, display_order)

        return super().create(validated_data)

    # ================= UPDATE =================
    def update(self, instance, validated_data):
        new_product = validated_data.get("product", instance.product)
        new_image = validated_data.get("image", None)
        is_primary = validated_data.get("is_primary", instance.is_primary)
        new_order = validated_data.get("display_order")

        # 1️⃣ LOGIC: Product change logic
        if new_product != instance.product:
            # Move image file physically if no new image is uploaded
            if not new_image:
                move_image(instance, new_product)
            
            # Handle order shifts in the NEW product
            instance.display_order = handle_product_change_order(instance, new_product, new_order)
            instance.product = new_product
        else:
            # Normal order update logic
            if new_order is not None:
                instance.display_order = handle_update_order(instance, new_order)

        # 2️⃣ LOGIC: Image replacement (Delete old)
        if new_image:
            if instance.image and os.path.exists(instance.image.path):
                os.remove(instance.image.path)
            instance.image = new_image

        # 3️⃣ LOGIC: Primary toggle logic
        if is_primary:
            Reward_Product_Image_model.objects.filter(product=instance.product).exclude(
                id=instance.id
            ).update(is_primary=False)
        instance.is_primary = is_primary

        # 4️⃣ OTHER FIELDS
        instance.is_active = validated_data.get("is_active", instance.is_active)

        instance.save()
        return instance
