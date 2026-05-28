# ============================================================
# FILE: models.py
# ============================================================

from django.db import models

# Django Default User Table
from django.contrib.auth.models import User


# ============================================================
# CART TABLE
# ============================================================

class Reward_Cart_Model(models.Model):

    STATUS_CHOICES = (
        ("active", "Active"),
        ("checked_out", "Checked Out"),
        ("abandoned", "Abandoned"),
    )

    # Login User
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id"
    )

    # Cart Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    # Total Cart Points
    total_points = models.IntegerField(default=0)

    # Date Time
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reward_cart"
        managed = False

    def __str__(self):
        return f"Cart {self.id} - {self.user.username}"