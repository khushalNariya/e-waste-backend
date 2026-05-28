# app_rewards/models.py

from django.db import models
from django.utils.text import slugify


class Reward_Category_model(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)  # Category name
    slug = models.SlugField(
        max_length=150, unique=True, blank=True
    )  # URL friendly name

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Auto-generate slug from name
        Example:
        "Gift Cards" → "gift-cards"
        """
        if not self.slug:
            base_slug = slugify(self.name)

            # 👉 Convert to Title Case
            base_slug = "-".join(word.capitalize() for word in base_slug.split("-"))

            slug = base_slug
            counter = 1

            # Ensure slug is unique
            while Reward_Category_model.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    class Meta:
        db_table = "reward_category"
        managed = False

    def __str__(self):
        return self.name