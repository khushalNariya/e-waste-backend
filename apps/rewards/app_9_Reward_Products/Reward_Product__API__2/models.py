# app_rewards/models.py

from django.db import models
from django.utils.text import slugify


class Reward_Product_model(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    category = models.ForeignKey("Reward_Category_model", on_delete=models.CASCADE)

    points = models.IntegerField()
    stock = models.IntegerField()

    description = models.TextField()
    terms = models.TextField(null=True, blank=True)

    tag = models.CharField(max_length=50, null=True, blank=True)
    delivery_days = models.CharField(max_length=50, null=True, blank=True)

    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    total_redeemed = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Auto slug generate
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Reward_Product_model.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    class Meta:
        db_table = "reward_products"
        managed = False

    def __str__(self):
        return self.name
