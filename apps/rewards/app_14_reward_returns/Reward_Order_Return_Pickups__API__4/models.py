from django.db import models
from app_14_reward_returns.Reward_Order_Return_Request__API__1.models import Reward_Order_Return_Request
from app_13_reward_orders.Reward_Order_Address__API__3.models import Reward_Order_Address

# Model mapping to return request courier pickup schedule details
class Reward_Order_Return_Pickup(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('picked_up', 'Picked Up'),
        ('failed', 'Failed'),
        ('rescheduled', 'Rescheduled'),
    )

    # Links the courier pickup record to parent return request
    return_request = models.ForeignKey(
        Reward_Order_Return_Request, 
        on_delete=models.CASCADE, 
        db_column='return_request_id', 
        related_name='pickups'
    )
    
    # Address details where the item must be picked up from
    order_address = models.ForeignKey(
        Reward_Order_Address, 
        on_delete=models.CASCADE, 
        db_column='order_address_id'
    )
    
    # Courier pickup tracking status
    pickup_status = models.CharField(
        max_length=30, 
        choices=STATUS_CHOICES, 
        default='scheduled'
    )

    class Meta:
        db_table = 'reward_order_return_pickups'
        managed = False

    def __str__(self):
        return f"Pickup for Return {self.return_request_id} ({self.pickup_status})"
