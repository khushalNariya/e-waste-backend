from django.db import models
from django.contrib.auth.models import User


# ===============================
# ORDER
# ===============================
class Reward_Order(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("processing", "Processing"),
        ("packed", "Packed"),
        ("shipped", "Shipped"),
        ("out_for_delivery", "Out For Delivery"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
        ("returned", "Returned"),
        ("failed", "Failed"),
    )

    order_number = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.IntegerField(null=True, blank=True)

    total_points = models.IntegerField()

    order_status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default="pending"
    )

    delivered_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Stores date and time when order is delivered"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reward_orders"
        managed = False

    def __str__(self):
        return self.order_number
