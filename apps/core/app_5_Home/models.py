# models.py

from django.db import models


class HowItWorks_model(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "home_page_how_it_works"   
        ordering = ['order']
        managed = False   

    def __str__(self):
        return self.title



class Hero_Section_model(models.Model):
    image = models.ImageField(upload_to="app_5_Home/hero/")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "home_page_hero_image"
        managed = False   

    def __str__(self):
        return "Hero Section"

     