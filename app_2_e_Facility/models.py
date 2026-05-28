from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    open_time = models.CharField(max_length=50)

    lat = models.FloatField()
    lon = models.FloatField()

    verified = models.BooleanField(default=False)



    class Meta:
        db_table = 'facility'
        managed = False
    
    def __str__(self):
        return self.name