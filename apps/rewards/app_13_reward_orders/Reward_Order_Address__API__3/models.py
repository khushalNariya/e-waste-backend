from django.db import models
from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order


# ===============================
# ORDER ADDRESS
# ===============================
class Reward_Order_Address(models.Model):

    order = models.OneToOneField(
        Reward_Order, on_delete=models.CASCADE, related_name="address"
    )

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    landmark = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "reward_order_address"
        managed = False

    def __str__(self):
        return f"Address for {self.order.order_number}"
