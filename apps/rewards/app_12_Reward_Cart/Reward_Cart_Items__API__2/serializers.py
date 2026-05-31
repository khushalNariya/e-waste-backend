from rest_framework import serializers
from .models import (
    Reward_Cart_Items_Model,
    
)





# ============================================================
# CART ITEM SERIALIZER
# ============================================================

class Reward_Cart_Items_Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    # Product Name
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    # Product Image
    product_image = serializers.SerializerMethodField()

    # Category Name
    category_name = serializers.CharField(
        source="product.category.name",
        read_only=True
    )

    # Product Stock
    product_stock = serializers.IntegerField(
        source="product.stock",
        read_only=True
    )

    email = serializers.EmailField(
        source="cart.user.email",
        read_only=True
    )

    user_name = serializers.SerializerMethodField()

    user_id = serializers.IntegerField(
        source="cart.user.id",
        read_only=True
    )

    def get_user_name(self, obj):
        return f"{obj.cart.user.first_name} {obj.cart.user.last_name}"

    class Meta:
        model = Reward_Cart_Items_Model
        fields = [
            "id",
            "cart",
            "user_id",
            "user_name",
            "email",
            "product",
            "product_name",
            "product_image",
            "product_stock",
            "category_name",
            "quantity",
            "points",
            "subtotal_points",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "points",
            "subtotal_points",
        ]

    # Product First Image
    def get_product_image(self, obj):

        image = obj.product.images.first()

        if image:
            request = self.context.get("request")

            if request:
                return request.build_absolute_uri(image.image.url)

        return None