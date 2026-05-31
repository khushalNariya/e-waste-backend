from django.db import models
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model


# images upload path
def product_image_upload_path(instance, filename):
    safe_name = instance.product.name.replace(" ", "_")
    return f"app_9_Reward_Products/Reward_Product_images/product_{instance.product.id}_{safe_name}/{filename}"


# reward product images model
class Reward_Product_Image_model(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(
        Reward_Product_model,
        on_delete=models.CASCADE,
        db_column="product_id",
        related_name="images",
    )
    image = models.ImageField(upload_to=product_image_upload_path)
    is_primary = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reward_product_images"
        managed = False
        unique_together = ("product", "display_order")
