from rest_framework import serializers
from app_5_Home.models import HowItWorks_model,Hero_Section_model
import os

# from .models import HowItWorks

class HowItWorks_Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
    format="%d %b %Y, %I:%M %p",
        read_only=True
    )

    updated_at = serializers.DateTimeField(
    format="%d %b %Y, %I:%M %p",
        read_only=True
    )


    title = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Title is required.",
            "blank": "Title cannot be empty."
        }
    )

    description = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Description is required.",
            "blank": "Description cannot be empty."
        }
    )

    icon = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Icon is required.",
            "blank": "Icon cannot be empty."
        }
    )

    order = serializers.IntegerField(
        required=False,
        error_messages={
            "invalid": "Order must be a number."
        }
    )

    is_active = serializers.BooleanField(required=False)

# =================== .Strim (White-Space) Remove ============================

    def validate(self, data):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data

# =================== Validations ============================

    # ========== Validation - 1 (Title) Field

    def validate_title(self, value):
        value = value.strip()

        qs = HowItWorks_model.objects.filter(title__iexact=value)

        # 🔥 EDIT case me current record exclude karo
        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError("Title already exists.")

        return value

    # ========== Validation - 2 (Order) Field

    def validate(self, data):
        # Example: Prevent duplicate order
        order = data.get("order")

        if order is not None:
            if HowItWorks_model.objects.filter(order=order).exclude(id=self.instance.id if self.instance else None).exists():
                raise serializers.ValidationError({
                    "order": "This order number is already assigned."
                })

        return data

    class Meta:
        model = HowItWorks_model
        fields = "__all__"


    
    

# ===========================================================================
# ================== Home-Page --- Hero Section =============================
# ===========================================================================

class Hero_Section_Serializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(
        format="%d %b %Y, %I:%M %p",
        read_only=True
    )

    updated_at = serializers.DateTimeField(
        format="%d %b %Y, %I:%M %p",
        read_only=True
    )

    class Meta:
        model = Hero_Section_model
        fields = "__all__"




    def validate(self, data):
        # 👇 Agar create request hai (instance nahi hai)
        if not self.instance:
            if not data.get("image"):
                raise serializers.ValidationError({
                    "image": "Image is required."
                })
        return data
    
    # ==================== Valiation (Option - 1) image , is_active

    # def update(self, instance, validated_data):

    #     new_image = validated_data.get("image", None)
    #     is_active = validated_data.get("is_active", instance.is_active)

    #     # -------- Image Replace --------

    #     # Agar new image aa rahi hai
    #     if new_image:
    #         # Old image exist karti hai?
    #         if instance.image and os.path.isfile(instance.image.path):
    #             os.remove(instance.image.path)

    #         instance.image = new_image

    # # -------- is_Active (Logic) --------
    #     if is_active:
    #         Hero_Section_model.objects.exclude(id=instance.id).update(is_active=False)

    #     instance.is_active = is_active
    #     instance.save()

    #     return instance

     # ================= IMAGE LOGIC =================

    def handle_image_replace(self, instance, new_image):

        # 👉 If new image is uploaded
        if new_image:

            # 👉 Delete old image from system (if exists)
            if instance.image and os.path.isfile(instance.image.path):
                os.remove(instance.image.path)

            # 👉 Set new image
            instance.image = new_image


    # ================= ACTIVE LOGIC =================

    def handle_active_logic(self, instance, is_active):

        # 👉 If current record is set to active
        if is_active:

            # 👉 Make all other records inactive
            Hero_Section_model.objects.exclude(id=instance.id).update(is_active=False)

        # 👉 Set current record active/inactive
        instance.is_active = is_active


    # ================= UPDATE =================
    
    def update(self, instance, validated_data):

        # 👉 Get new image (if provided)
        new_image = validated_data.get("image", None)

        # 👉 Get is_active value (or keep old one)
        is_active = validated_data.get("is_active", instance.is_active)

        # 👉 Call image replace logic
        self.handle_image_replace(instance, new_image)

        # 👉 Call active logic
        self.handle_active_logic(instance, is_active)

        # 👉 Save final changes
        instance.save()

        return instance