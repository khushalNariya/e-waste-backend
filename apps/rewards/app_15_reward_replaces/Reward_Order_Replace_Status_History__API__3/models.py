from django.db import models
from django.contrib.auth.models import User
from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.models import Reward_Order_Replace_Request


# Audit trail model tracking every status change in a replace request
class Reward_Order_Replace_Status_History(models.Model):

    # Links this log entry to its parent replace request
    replace_request = models.ForeignKey(
        Reward_Order_Replace_Request,
        on_delete=models.CASCADE,
        db_column='replace_request_id',
        related_name='status_history'
    )

    # The new status this request was changed TO
    status = models.CharField(max_length=50)

    # Who made this status change (admin or user). NULL if system-generated
    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='changed_by'
    )

    # Internal note or reason for this status change
    remarks = models.TextField(null=True, blank=True)

    # Log creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # Log last updated timestamp
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reward_order_replace_status_history'
        managed = False

    def __str__(self):
        return f"Replace {self.replace_request_id} - {self.status}"
