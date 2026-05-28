from django.db import models

class Recycle_Category(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    process = models.TextField()
    instruction = models.TextField()
    benefits = models.TextField()
    button_text = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)   # create
    updated_at = models.DateTimeField(auto_now=True)       # update



    class Meta:
        db_table = 'recycling_info'
        managed = False
    
    def __str__(self):
        return self.title