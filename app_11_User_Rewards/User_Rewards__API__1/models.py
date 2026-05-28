from django.db import models
from django.contrib.auth.models import User
from app_10_E_Waste_Submission.E_Waste_Submission__API__1.models import (
    E_Waste_Submission_Model,
)


# ===============================
# 🔹 USER WALLET MODEL
# ===============================
class User_Wallet_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")

    total_points = models.IntegerField(default=0)  # 👈 current balance

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_wallet"
        managed = False  # ⚠️ because table already MySQL me hai

    def __str__(self):
        return f"{self.user.username} - {self.total_points} pts"


from app_13_reward_orders.Reward_Order__API__1.models import Reward_Order


# ===============================
# 🔹 REWARD TRANSACTION MODEL
# ===============================
class Reward_Transaction_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")

    submission = models.ForeignKey(
        # E_Waste_Submission_Model, on_delete=models.CASCADE, db_column="submission_id"
        E_Waste_Submission_Model,
        on_delete=models.CASCADE,
        db_column="submission_id",
        null=True,
        blank=True,
    )

    # Added for Reward Orders
    order = models.ForeignKey(
        Reward_Order,
        on_delete=models.CASCADE,
        db_column="order_id",
        null=True,
        blank=True,
    )

    points = models.IntegerField()

    type = models.CharField(
        max_length=10,
        choices=(("credit", "Credit"), ("debit", "Debit")),
        default="credit",
    )

    description = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reward_transactions"
        managed = False

    def __str__(self):
        return f"{self.user.username} - {self.points} pts ({self.type})"
