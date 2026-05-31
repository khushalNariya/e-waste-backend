from django.db import models
from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order

# ===============================
# ORDER PAYMENT
# ===============================
class Reward_Order_Payment(models.Model):

    order = models.OneToOneField(
        Reward_Order,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)

    amount_points = models.IntegerField(default=0)
    amount_money = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        db_table = "reward_order_payments"
        managed = False

        
    def __str__(self):
        return f"Payment for {self.order.order_number}"
