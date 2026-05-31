from django.db import models
from django.utils import timezone
from app_14_reward_returns.Reward_Order_Return_Request__API__1.models import Reward_Order_Return_Request

# Custom image upload path generator matching app_10 style
def return_image_upload_path(instance, filename):
    user = instance.return_request.user
    return_id = instance.return_request.id
    
    # Extract and clean first name and last name
    first_name = (user.first_name or "").strip().replace(" ", "_")
    last_name = (user.last_name or "").strip().replace(" ", "_")
    full_name = f"{first_name}_{last_name}".strip("_")
    
    # Fallback if names are blank
    if not full_name:
        full_name = f"user_{user.username}"
        
    date = timezone.now().strftime("%Y-%m-%d")
    
    # Clean output path structure
    return (
        f"app_14_reward_returns/"
        f"reward_return_images/"
        f"user_{user.id}_{full_name}/"
        f"return_{return_id}/"
        f"{date}/{filename}"
    )

# Model representing return request upload proofs
class Reward_Order_Return_Image(models.Model):
    # Foreign key links proof photos to parent return request
    return_request = models.ForeignKey(
        Reward_Order_Return_Request,
        on_delete=models.CASCADE,
        db_column='return_request_id',
        related_name='images'
    )
    
    # Path pointer or actual binary handler of returned product image file
    image = models.ImageField(upload_to=return_image_upload_path, max_length=255, db_column='image_path')
    
    # Upload registration timestamp
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'reward_order_return_images'
        managed = False

    def __str__(self):
        return f"Image for Return Request {self.return_request_id}"
