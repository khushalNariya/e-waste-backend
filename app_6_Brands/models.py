from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)   # create
    updated_at = models.DateTimeField(auto_now=True)       # update

    class Meta:
        db_table = 'brand'
        managed = False

    def __str__(self):
        return self.name