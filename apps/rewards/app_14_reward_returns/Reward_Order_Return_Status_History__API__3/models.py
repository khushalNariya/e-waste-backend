from django.db import models
from django.contrib.auth.models import User
from app_14_reward_returns.Reward_Order_Return_Request__API__1.models import Reward_Order_Return_Request

# Audit trail model tracking status transitions
class Reward_Order_Return_Status_History(models.Model):
    # Foreign key links history logs to parent return request
    return_request = models.ForeignKey(
        Reward_Order_Return_Request, 
        on_delete=models.CASCADE, 
        db_column='return_request_id', 
        related_name='status_history'
    )
    
    # Label of the new status updated to
    status = models.CharField(max_length=50)
    
    # Links to user (Admin or Customer Care) who changed the status
    changed_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        db_column='changed_by'
    )
    
    # Internal text log comment / reason for this change
    remarks = models.TextField(null=True, blank=True)
    
    # Log creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Log update timestamp
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reward_order_return_status_history'
        managed = False

    def __str__(self):
        return f"Return {self.return_request_id} - {self.status}"
