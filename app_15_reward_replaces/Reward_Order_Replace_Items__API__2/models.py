from django.db import models
from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.models import Reward_Order_Replace_Request
from app_13_reward_orders.Reward_Order_Items__API__2.models import Reward_Order_Item
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model


# Model for individual items inside a replace request
class Reward_Order_Replace_Item(models.Model):

    # Links this item to its parent replace request
    replace_request = models.ForeignKey(
        Reward_Order_Replace_Request,
        on_delete=models.CASCADE,
        db_column='replace_request_id',
        related_name='items'
    )

    # Links to the original order item being replaced
    order_item = models.ForeignKey(
        Reward_Order_Item,
        on_delete=models.CASCADE,
        db_column='order_item_id'
    )

    # Original product reference
    product = models.ForeignKey(
        Reward_Product_model,
        on_delete=models.CASCADE,
        db_column='product_id'
    )

    # Snapshot of original product name at time of request
    product_name = models.CharField(max_length=255)

    # Quantity being replaced
    quantity = models.IntegerField(default=1)

    # Points per unit at time of original order
    points = models.IntegerField()

    # Total points: quantity x points
    subtotal_points = models.IntegerField()

    # Condition/issue reported by user (wrong_item, defective, damaged, wrong_color)
    item_condition = models.CharField(max_length=100, null=True, blank=True)

    # Replacement product (NULL = same item, set when different variant requested)
    replacement_product = models.ForeignKey(
        Reward_Product_model,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='replacement_product_id',
        related_name='replacement_items'
    )

    # Snapshot of the replacement product name (NULL if same item)
    replacement_product_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'reward_order_replace_items'
        managed = False

    def __str__(self):
        return f"{self.product_name} ({self.quantity})"
