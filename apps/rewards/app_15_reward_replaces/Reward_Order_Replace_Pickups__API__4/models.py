from django.db import models
from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.models import Reward_Order_Replace_Request
from app_13_reward_orders.Reward_Order_Address__API__3.models import Reward_Order_Address


# Model for courier pickup + delivery details (Amazon-style: one trip does both)
class Reward_Order_Replace_Pickup(models.Model):

    STATUS_CHOICES = (
        ('scheduled',   'Scheduled'),
        ('picked_up',   'Picked Up'),
        ('failed',      'Failed'),
        ('rescheduled', 'Rescheduled'),
    )

    # Links this pickup record to its parent replace request
    replace_request = models.ForeignKey(
        Reward_Order_Replace_Request,
        on_delete=models.CASCADE,
        db_column='replace_request_id',
        related_name='pickups'
    )

    # Address where old item will be picked up from (same as delivery usually)
    order_address = models.ForeignKey(
        Reward_Order_Address,
        on_delete=models.CASCADE,
        db_column='order_address_id'
    )

    # Pickup status of the old item collection
    pickup_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='scheduled')

    # Address where new replacement item will be delivered (usually same as pickup)
    delivery_address = models.ForeignKey(
        Reward_Order_Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='delivery_address_id',
        related_name='replace_deliveries'
    )

    # Courier partner name (e.g. BlueDart, Delhivery)
    courier_name = models.CharField(max_length=100, null=True, blank=True)

    # Tracking number for the replacement shipment
    tracking_number = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'reward_order_replace_pickups'
        managed = False

    def __str__(self):
        return f"Pickup for Replace {self.replace_request_id} ({self.pickup_status})"
