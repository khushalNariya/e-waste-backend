from django.db import models
from django.utils.text import slugify


class EducationArticle_model(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)

    description = models.TextField()
    # image = models.CharField(max_length=500)
    # image = models.ImageField(upload_to="education_images/")

    # image = models.ImageField(upload_to="")
    image = models.ImageField(upload_to="app_4_Education/education_images/")

    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    readTime = models.CharField(max_length=20)
    isFeatured = models.BooleanField(default=False)
    Education_Create_at = models.DateTimeField(auto_now_add=True)
    Education_Update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while EducationArticle_model.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        db_table = "education_article"
        managed = False
