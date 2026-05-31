from django.db import models
from django.contrib.auth.models import User
from app_3_Recycling_info.models import Recycle_Category
from app_7_Category_Brand_Mapping.models import (
    Category_Brand_Mapping_Model,
    Product_Model_Name_Model,
)
from app_8_Reward_Rules.models import Item_Condition_model
from app_2_e_Facility.models import Facility


class E_Waste_Submission_Model(models.Model):
    STATUS_CHOICES = [
        ("requested", "Requested"),
        ("picked_up_dropped_off", "Picked Up/Dropped Off"),
        ("evaluating", "Evaluating"),
        ("recycled", "Recycled"),
        ("rewarded", "Rewarded"),
        ("rejected", "Rejected"),
    ]

    PICKUP_CHOICES = (
        ("pickup", "Pickup"),
        ("dropoff", "Dropoff"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    category = models.ForeignKey(
        Recycle_Category, on_delete=models.CASCADE, db_column="category_id"
    )
    category_brand_mapping = models.ForeignKey(
        Category_Brand_Mapping_Model,
        on_delete=models.CASCADE,
        db_column="category_brand_mapping_id",
    )
    model = models.ForeignKey(
        Product_Model_Name_Model, on_delete=models.CASCADE, db_column="model_id"
    )
    user_condition = models.ForeignKey(
        Item_Condition_model,
        on_delete=models.CASCADE,
        db_column="user_condition_id",
        related_name="user_submissions",
    )
    final_condition = models.ForeignKey(
        Item_Condition_model,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="final_condition_id",
        related_name="admin_submissions",
    )
    weight = models.FloatField(null=True, blank=True)
    pickup_type = models.CharField(max_length=10, choices=PICKUP_CHOICES)
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, db_column="facility_id"
    )

    address = models.TextField()
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    phone = models.CharField(max_length=20)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="requested"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "e_waste_submission"
        managed = False

    def __str__(self):
        return f"Submission {self.id} by {self.user.username}"
