from django.db import models
from django.contrib.auth.models import User
from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order


class Reward_Order_Status_History(models.Model):
    order = models.ForeignKey(
        Reward_Order,
        on_delete=models.CASCADE,
        db_column="order_id",
        related_name="status_history",
    )
    status = models.CharField(max_length=50)
    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="changed_by",
    )
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reward_order_status_history"
        managed = False

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"
