from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user_1 = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        db_column="table_auth_user_id",  # EXACT MATCH with DB
    )

    Show_Password = models.CharField(max_length=300)

    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    user_created_on = models.DateTimeField()
    user_updated_on = models.DateTimeField()
    # user_created_on = models.DateTimeField(auto_now_add=True)  # create time
    # user_updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "accounts_user_profile"
        managed = False
