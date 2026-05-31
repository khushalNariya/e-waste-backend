from django.db import models
from app_10_E_Waste_Submission.E_Waste_Submission__API__1.models import (
    E_Waste_Submission_Model,
)

from django.utils import timezone


# images upload path
def e_waste_image_upload_path(instance, filename):
    user = instance.submission.user
    submission_id = instance.submission.id

    # 👇 First + Last Name
    first_name = (user.first_name or "").strip().replace(" ", "_")
    last_name = (user.last_name or "").strip().replace(" ", "_")

    full_name = f"{first_name}_{last_name}".strip("_")

    date = timezone.now().strftime("%Y-%m-%d")

    return (
        f"app_10_E_Waste_Submission/"
        f"e_waste_form_submit_images/"
        f"user_{user.id}_{full_name}/"
        f"submission_{submission_id}/"
        f"{date}/{filename}"
    )


# e waste submission images model
class E_Waste_Submission_Images_Model(models.Model):
    submission = models.ForeignKey(
        E_Waste_Submission_Model,
        on_delete=models.CASCADE,
        db_column="submission_id",
        related_name="images",
    )
    image = models.ImageField(upload_to=e_waste_image_upload_path, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = "e_waste_submission_images"
        managed = False

    def __str__(self):
        return f"Image for Submission {self.submission_id}"
