from django.db import models
from app_14_reward_returns.Reward_Order_Return_Request__API__1.models import Reward_Order_Return_Request
from app_13_reward_orders.Reward_Order_Items__API__2.models import Reward_Order_Item
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model

# Model mapping to return request individual items
class Reward_Order_Return_Item(models.Model):
    # Foreign key links the item to its parent return request
    return_request = models.ForeignKey(
        Reward_Order_Return_Request, 
        on_delete=models.CASCADE, 
        db_column='return_request_id', 
        related_name='items'
    )
    
    # Links return item back to the original order item
    order_item = models.ForeignKey(
        Reward_Order_Item, 
        on_delete=models.CASCADE, 
        db_column='order_item_id'
    )
    
    # Links return item to the reward product model
    product = models.ForeignKey(
        Reward_Product_model, 
        on_delete=models.CASCADE, 
        db_column='product_id'
    )
    
    # Snapshot name of the returned product
    product_name = models.CharField(max_length=255)
    
    # Quantity of the product returned
    quantity = models.IntegerField(default=1)
    
    # Reward points for a single quantity of the product
    points = models.IntegerField()
    
    # Total refund points for this returned item (qty * points)
    subtotal_points = models.IntegerField()
    
    # Description of the item's physical condition (e.g. damaged, wrong_item, used)
    item_condition = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'reward_order_return_items'
        managed = False

    def __str__(self):
        return f"{self.product_name} ({self.quantity})"
