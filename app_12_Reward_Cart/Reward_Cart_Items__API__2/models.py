# ============================================================
# FILE: models.py
# ============================================================

from django.db import models

# Cart Model
from app_12_Reward_Cart.Reward_Cart__API__1.models import Reward_Cart_Model

# Reward Product Model
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model


# ============================================================
# CART ITEMS TABLE
# ============================================================

class Reward_Cart_Items_Model(models.Model):

    # Main Cart
    cart = models.ForeignKey(
        Reward_Cart_Model,
        on_delete=models.CASCADE,
        db_column="cart_id",
        related_name="cart_items"
    )

    # Reward Product
    product = models.ForeignKey(
        Reward_Product_model,
        on_delete=models.CASCADE,
        db_column="product_id"
    )

    # Quantity
    quantity = models.IntegerField(default=1)

    # Product Points Snapshot
    points = models.IntegerField()

    # Total Points
    subtotal_points = models.IntegerField()

    # Date Time
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reward_cart_items"
        managed = False

    def __str__(self):
        return f"{self.product.name} - Qty {self.quantity}"