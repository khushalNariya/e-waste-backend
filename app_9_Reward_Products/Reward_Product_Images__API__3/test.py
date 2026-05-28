# serializers.py

from rest_framework import serializers
from .models import Reward_Product_model, Reward_Product_Image_model
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model
import os
from django.db import transaction
from django.db import models  # 🔥 ADD at top if not present
from django.db.models import F
import random

# ===============================
# 🔹 MINI SERIALIZERS (ONLY FOR MAPPING)
# ===============================


class Reward_Product_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reward_Product_model
        fields = ["id", "name"]  # 👈 only required


# ===============================
# 🔹 MAIN MAPPING SERIALIZER
# ===============================


class Reward_Product_Image_Serializer(serializers.ModelSerializer):

    # ✅ READ (GET → {} format with name)
    product = Reward_Product_Mini_Serializer(read_only=True)

    # ✅ WRITE (POST → id pass karo)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Reward_Product_model.objects.all(), source="product", write_only=True
    )

    # ✅ DATE FORMAT (optional but good)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    class Meta:
        model = Reward_Product_Image_model
        fields = [
            "id",
            "product",
            "product_id",
            "image",
            "is_primary",
            "display_order",
            "is_active",
            "created_at",
            "updated_at",
        ]

    # ====================================================
    # ================= FIELD VALIDATION =================
    # ====================================================

    image = serializers.ImageField(
        required=True,
        # allow_blank=False,
        error_messages={
            "required": "Image is required",
            "blank": "Image cannot be empty",
        },
    )
    is_primary = serializers.BooleanField(
        required=True,
        # allow_blank=False,
        error_messages={
            "required": "is_primary is required",
            "blank": "is_primary cannot be empty",
            "invalid": "Invalid boolean value",
        },
    )

    display_order = serializers.IntegerField(
        required=False,
        allow_null=True,  # 🔥 ADD THIS
        default=None,  # 🔥 ADD THIS
        error_messages={
            "required": "Display order is required",
            "invalid": "Invalid display order value",
            "blank": "Display order cannot be empty",
        },
    )

    is_active = serializers.BooleanField(required=False, default=True)

    # =====================================================
    # ================= COMMON VALIDATION =================
    # =====================================================

    def validate(self, data):
        """
        Step 1: Trim all string fields (remove spaces)
        Step 2: Check image required on create only
        """

        # TRIM ALL FIELDS
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        # 🔥 THIS IS MAIN FIX
        if "display_order" not in data or data.get("display_order") in ["", None]:
            data["display_order"] = None

        # IMAGE REQUIRED ONLY ON CREATE (Only allow image on create request)
        if not self.instance:
            if not data.get("image"):
                raise serializers.ValidationError({"image": "Image is required."})
        return data

    # =========================================
    # ================================ Re-Use-Able Methods ===================================
    # =========================================

    # ------------------------------------------------
    # ================= IMAGE UPDATE =================
    # ------------------------------------------------

    def handle_image_replace(self, instance, new_image):
        """
        If new image uploaded → delete old image
        """

        # 👉 Check if new image is provided
        if new_image:
            # 👉 If old image exists in system, delete it
            if instance.image and os.path.isfile(instance.image.path):
                os.remove(instance.image.path)

            # 👉 Set new image
            instance.image = new_image

    # ------------------------------------------------
    # ================= ACTIVE LOGIC =================
    # ------------------------------------------------

    def handle_active_logic(self, instance, is_primary):
        """
        Ensure only ONE image is primary per product
        """

        # 👉 If current image is set as primary
        if is_primary:

            # 👉 Make all other images of SAME product non-primary
            Reward_Product_Image_model.objects.filter(product=instance.product).exclude(
                id=instance.id
            ).update(is_primary=False)

        # 👉 Set current record primary/non-primary
        instance.is_primary = is_primary

    # ------------------------------------------------
    # ================= ORDER LOGIC =================
    # ------------------------------------------------

    # def handle_order_logic(self, instance, new_order):
    #     """
    #     Maintain proper ordering when display_order changes
    #     """

    #     old_order = instance.display_order

    #     # 👉 If order is changed
    #     if new_order != old_order:

    #         # CASE 1: Move DOWN (2 → 5)
    #         if new_order > old_order:
    #             Reward_Product_Image_model.objects.filter(
    #                 product=instance.product,  # ✅ ADD THIS LINE
    #                 display_order__gt=old_order,
    #                 display_order__lte=new_order,
    #             ).update(display_order=F("display_order") - 1)

    #         # CASE 2: Move UP (5 → 2)
    #         else:
    #             Reward_Product_Image_model.objects.filter(
    #                 product=instance.product,  # ✅ ADD THIS LINE
    #                 display_order__gte=new_order,
    #                 display_order__lt=old_order,
    #             ).update(display_order=F("display_order") + 1)

    #     # 👉 Set new order
    #     instance.display_order = new_order

    def handle_order_logic(self, instance, new_order, new_product):

        old_order = instance.display_order
        old_product = instance.product

        # 👉 SAME PRODUCT
        if new_product == old_product:

            # 🔥 CHECK: kya new_order already exist karta hai?
            exists = Reward_Product_Image_model.objects.filter(
                product=old_product,
                display_order=new_order
            ).exclude(id=instance.id).exists()

            # 👉 ONLY SHIFT if conflict
            if exists:

                # MOVE DOWN
                if new_order > old_order:
                    Reward_Product_Image_model.objects.filter(
                        product=old_product,
                        display_order__gt=old_order,
                        display_order__lte=new_order
                    ).update(display_order=F("display_order") - 1)

                # MOVE UP
                elif new_order < old_order:
                    Reward_Product_Image_model.objects.filter(
                        product=old_product,
                        display_order__gte=new_order,
                        display_order__lt=old_order
                    ).update(display_order=F("display_order") + 1)

        else:
            # PRODUCT CHANGE (same as before)
            Reward_Product_Image_model.objects.filter(
                product=old_product,
                display_order__gt=old_order
            ).update(display_order=F("display_order") - 1)

            Reward_Product_Image_model.objects.filter(
                product=new_product,
                display_order__gte=new_order
            ).update(display_order=F("display_order") + 1)

            instance.product = new_product

        instance.display_order = new_order

    # =======================================================================
    # =================== CREATE ===================
    # =======================================================================

    def create(self, validated_data):

        with transaction.atomic():

            # 👉 Get order from request (if user provided)
            order = validated_data.get("display_order")

            # ===============================
            # 👉 CASE 1: User PROVIDED order
            # ===============================
            if order is not None:

                # 🔥 STEP 1: safe temp value (conflict avoid)
                validated_data["display_order"] = 9999

                # 👉 Shift all images of SAME product
                Reward_Product_Image_model.objects.filter(
                    product=validated_data["product"], display_order__gte=order
                ).update(display_order=models.F("display_order") + 1)

                # 🔥 STEP 3: final correct order set
                validated_data["display_order"] = order

            # ===============================
            # 👉 CASE 2: User DID NOT provide order
            # ===============================
            else:
                last = (
                    Reward_Product_Image_model.objects.filter(
                        product=validated_data["product"]
                    )
                    .order_by("-display_order")
                    .first()
                )

                if last:
                    validated_data["display_order"] = last.display_order + 1
                else:
                    validated_data["display_order"] = 1

            return super().create(validated_data)

    # =======================================================================
    # =================== UPDATE ===================
    # =======================================================================

    def update(self, instance, validated_data):

        with transaction.atomic():  # ✅ ADD THIS

            # 👉 Get new image (if provided)
            new_image = validated_data.get("image", None)
            # 👉 1. Call (Image logic) Function
            self.handle_image_replace(instance, new_image)

            # 👉 Get is_active value (or keep old one)
            is_primary = validated_data.get("is_primary", instance.is_primary)
            # 👉 2. Call (Active logic) Function
            self.handle_active_logic(instance, is_primary)

            # 👉 Get new order (or keep old one)
            new_order = validated_data.get("display_order", instance.display_order)
            # 🔥 NEW LINE ADD
            new_product = validated_data.get("product", instance.product)
            # 🔥 STEP 1: temp safe value
            temp_order = random.randint(10000, 99999)
            instance.display_order = temp_order
            instance.save()
            # 3 Call (Order logic) Function
            self.handle_order_logic(instance, new_order, new_product)

            # 👉 Update other simple fields
            instance.is_active = validated_data.get("is_active", instance.is_active)

            # 👉 Save final changes
            instance.save()

            return instance


# =======================================================================
# =======================================================================
# =======================================================================
# =======================================================================
# =======================================================================
# =======================================================================
# =======================================================================
# serializers.py

from rest_framework import serializers
from .models import Reward_Product_model, Reward_Product_Image_model
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model
import os

# ===============================
# 🔹 MINI SERIALIZERS (ONLY FOR MAPPING)
# ===============================


class Reward_Product_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reward_Product_model
        fields = ["id", "name"]  # 👈 only required


# ===============================
# 🔹 MAIN MAPPING SERIALIZER
# ===============================


class Reward_Product_Image_Serializer(serializers.ModelSerializer):

    # ✅ READ (GET → {} format with name)
    product = Reward_Product_Mini_Serializer(read_only=True)

    # ✅ WRITE (POST → id pass karo)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Reward_Product_model.objects.all(), source="product", write_only=True
    )

    # ✅ DATE FORMAT (optional but good)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    class Meta:
        model = Reward_Product_Image_model
        fields = [
            "id",
            "product",
            "product_id",
            "image",
            "is_primary",
            "display_order",
            "is_active",
            "created_at",
            "updated_at",
        ]

    # ================= FIELD VALIDATION =================
    image = serializers.ImageField(
        required=True,
        # allow_blank=False,
        error_messages={
            "required": "Image is required",
            "blank": "Image cannot be empty",
        },
    )
    is_primary = serializers.BooleanField(
        required=True,
        # allow_blank=False,
        error_messages={
            "required": "is_primary is required",
            "blank": "is_primary cannot be empty",
            "invalid": "Invalid boolean value",
        },
    )

    display_order = serializers.IntegerField(
        required=False,
        allow_null=True,
        error_messages={
            "required": "Display order is required",
            "invalid": "Invalid display order value",
            "blank": "Display order cannot be empty",
        },
    )

    is_active = serializers.BooleanField(required=False, default=True)

    # ================= COMMON VALIDATION =================
    def validate(self, data):
        """
        Step 1: Trim all string fields (remove spaces)
        Step 2: Check image required on create only
        """

        # TRIM ALL FIELDS
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        # IMAGE REQUIRED ONLY ON CREATE (Only allow image on create request)
        if not self.instance:
            if not data.get("image"):
                raise serializers.ValidationError({"image": "Image is required."})
        return data

    # ================= IMAGE UPDATE =================

    # def update(self, instance, validated_data):

    #     """
    #     If new image uploaded → delete old image
    #     """

    #     new_image = validated_data.get("image", None)

    #     # Agar new image aa rahi hai
    #     if new_image:
    #         # Old image exist karti hai?
    #         if instance.image and os.path.isfile(instance.image.path):
    #             os.remove(instance.image.path)

    #     return super().update(instance, validated_data)

    # ================= ACTIVE LOGIC =================

    def handle_active_logic(self, instance, is_primary):

        # 👉 If current record is set to active
        if is_primary:

            # 👉 Make all other records inactive
            Reward_Product_Image_model.objects.filter(
                product=instance.product
            ).exclude(id=instance.id).update(is_primary=False)

        # 👉 Set current record active/inactive
        instance.is_primary = is_primary

    # ================= UPDATE =================

    # def update(self, instance, validated_data):

    #     # 👉 Get new image (if provided)
    #     new_image = validated_data.get("image", None)

    #     # 👉 Get is_active value (or keep old one)
    #     is_primary = validated_data.get("is_primary", instance.is_primary)

    #     # 👉 Call image replace logic
    #     self.handle_image_replace(instance, new_image)

    #     # 👉 Call active logic
    #     self.handle_active_logic(instance, is_primary)

    #     # 👉 Save final changes
    #     instance.save()

    #     return instance

    def update(self, instance, validated_data):

        new_image = validated_data.get("image", None)
        is_primary = validated_data.get("is_primary", instance.is_primary)

        # ================= IMAGE REPLACE =================
        if new_image:
            # if instance.image and os.path.isfile(instance.image.path):
            #     os.remove(instance.image.path)
            if instance.image and hasattr(instance.image, "path") and os.path.exists(instance.image.path):
                os.remove(instance.image.path)

            instance.image = new_image

        # ================= PRIMARY LOGIC =================
        if is_primary:
            Reward_Product_Image_model.objects.filter(product=instance.product).exclude(
                id=instance.id
            ).update(is_primary=False)

        instance.is_primary = is_primary

        # ================= OTHER FIELDS =================
        instance.display_order = validated_data.get(
            "display_order", instance.display_order
        )
        instance.is_active = validated_data.get("is_active", instance.is_active)

        instance.save()

        return instance





# ===========================================================
# ===========================================================
# ===========================================================
# views.py

from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from .models import Reward_Product_Image_model
from .serializers import Reward_Product_Image_Serializer

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# pagi
from ..Pagination__File.pagination import user__Pagination


class Reward_Product_Image_ViewSet(ModelViewSet):

    queryset = Reward_Product_Image_model.objects.all().order_by('product_id','display_order')
    serializer_class = Reward_Product_Image_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = [
        "product__name",
    ]

    ordering_fields = ["id", "display_order", "created_at"]

    pagination_class = user__Pagination

    # Partial update support
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
