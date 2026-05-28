from django.db import models
from django.contrib.auth.models import User
from app_10_E_Waste_Submission.E_Waste_Submission__API__1.models import E_Waste_Submission_Model


class E_Waste_Status_History_Model(models.Model):
    submission = models.ForeignKey(
        E_Waste_Submission_Model,
        on_delete=models.CASCADE,
        db_column="submission_id",
        related_name="status_history"
    )

    status = models.CharField(max_length=50)

    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="changed_by"
    )

    remarks = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "e_waste_status_history"
        managed = False

    def __str__(self):
        return f"{self.submission_id} - {self.status}"