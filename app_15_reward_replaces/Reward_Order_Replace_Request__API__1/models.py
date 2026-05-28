from django.db import models
from django.contrib.auth.models import User
from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order


# Main table model for replace requests (Amazon-style)
class Reward_Order_Replace_Request(models.Model):

    # Available status transitions for the replace flow
    STATUS_CHOICES = (
        ('requested',               'Requested'),
        ('approved',                'Approved'),
        ('replacement_dispatched',  'Replacement Dispatched'),
        ('replacement_delivered',   'Replacement Delivered'),
        ('rejected',                'Rejected'),
    )

    # Replace type choices
    REPLACE_TYPE_CHOICES = (
        ('same_item',        'Same Item'),
        ('different_variant','Different Variant'),
    )

    # Unique identifier for the replace request (e.g. REP-20250522143000)
    replace_number = models.CharField(max_length=50, unique=True)

    # Links replace request to the original delivered order
    order = models.ForeignKey(Reward_Order, on_delete=models.CASCADE, db_column='order_id')

    # Links replace request to the user who submitted it
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    # Current status of this replace request
    replace_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='requested')

    # Reason for replacement (e.g. wrong item, defective, damaged)
    replace_reason = models.CharField(max_length=255)

    # Optional extra note from user about the issue
    replace_note = models.TextField(null=True, blank=True)

    # Whether user wants same item or a different variant
    replace_type = models.CharField(max_length=30, choices=REPLACE_TYPE_CHOICES, default='same_item')

    # Scheduled date for replacement delivery + old item pickup (set by admin)
    replace_date = models.DateTimeField(null=True, blank=True)

    # Creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # Last update timestamp
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reward_order_replace_requests'
        managed = False

    def __str__(self):
        return f"{self.replace_number} - {self.replace_status}"
