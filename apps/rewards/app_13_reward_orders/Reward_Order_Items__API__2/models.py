from django.db import models
from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order


# ===============================
# ORDER ITEMS
# ===============================
class Reward_Order_Item(models.Model):

    order = models.ForeignKey(
        Reward_Order, on_delete=models.CASCADE, related_name="items"
    )

    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)

    quantity = models.IntegerField()
    points = models.IntegerField()
    subtotal_points = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reward_order_items"
        managed = False

    def __str__(self):
        return f"{self.product_name} ({self.quantity})"
