from django.db import models
from django.contrib.auth.models import User
from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order

# Main table model for return requests
class Reward_Order_Return_Request(models.Model):
    # Available status transitions for return request
    STATUS_CHOICES = (
        ('requested', 'Requested'),
        ('approved', 'Approved'),
        ('pickup_scheduled', 'Pickup Scheduled'),
        ('picked_up', 'Picked Up'),
        ('received', 'Received'),
        ('inspected', 'Inspected'),
        ('refund_approved', 'Refund Approved'),
        ('refunded', 'Refunded'),
        ('rejected', 'Rejected'),
    )

    # Unique identifier of the return request (e.g. RET-001)
    return_number = models.CharField(max_length=50, unique=True)
    
    # ForeignKey links return request to reward order
    order = models.ForeignKey(Reward_Order, on_delete=models.CASCADE, db_column='order_id')
    
    # ForeignKey links return request to the user submitting it
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    
    # Current status of the return flow
    return_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='requested')
    
    # Reason for the return request
    return_reason = models.CharField(max_length=255)
    
    # Optional comment/note from the user about the return
    return_note = models.TextField(null=True, blank=True)
    
    # Points to be refunded upon successful return processing
    refund_points = models.IntegerField(default=0)
    
    # Scheduled return pickup date and time
    return_date = models.DateTimeField(null=True, blank=True)
    
    # Creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Last update timestamp
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reward_order_return_requests'
        managed = False

    def __str__(self):
        return f"{self.return_number} - {self.return_status}"
