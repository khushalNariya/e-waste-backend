from django.db import models
from django.utils import timezone
from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.models import Reward_Order_Replace_Request


# Custom upload path builder for replace proof images
def replace_image_upload_path(instance, filename):
    user = instance.replace_request.user
    replace_id = instance.replace_request.id

    # Build clean name from user's first and last name
    first_name = (user.first_name or "").strip().replace(" ", "_")
    last_name  = (user.last_name  or "").strip().replace(" ", "_")
    full_name  = f"{first_name}_{last_name}".strip("_")

    # Fallback if names are empty
    if not full_name:
        full_name = f"user_{user.username}"

    date = timezone.now().strftime("%Y-%m-%d")

    return (
        f"app_15_reward_replaces/"
        f"replace_images/"
        f"user_{user.id}_{full_name}/"
        f"replace_{replace_id}/"
        f"{date}/{filename}"
    )


# Model representing proof images uploaded by user for replace request
class Reward_Order_Replace_Image(models.Model):

    # Links this image to its parent replace request
    replace_request = models.ForeignKey(
        Reward_Order_Replace_Request,
        on_delete=models.CASCADE,
        db_column='replace_request_id',
        related_name='images'
    )

    # Actual image file stored at the generated upload path
    image = models.ImageField(upload_to=replace_image_upload_path, max_length=255, db_column='image_path')

    # Timestamp when image was uploaded
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'reward_order_replace_images'
        managed = False

    def __str__(self):
        return f"Image for Replace Request {self.replace_request_id}"
