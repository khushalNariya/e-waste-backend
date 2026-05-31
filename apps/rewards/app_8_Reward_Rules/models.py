from django.db import models

class Item_Condition_model(models.Model):
    name = models.CharField(max_length=50, unique=True)          # system use (like_new)
    display_name = models.CharField(max_length=100)               # UI show (Like New)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item_conditions'
        managed = False

    def __str__(self):
        return self.display_name

# ========================================================================
# ================ Reward - Rules  ================================
# ========================================================================

class Reward_Rule_model(models.Model):
    UNIT_CHOICES = (
        ('item', 'Item'),
        ('kg', 'Kg'),
    )

    category = models.ForeignKey(
        'app_3_Recycling_info.Recycle_Category', 
        on_delete=models.CASCADE
    )
    condition = models.ForeignKey(
        'app_8_Reward_Rules.Item_Condition_model', 
        on_delete=models.CASCADE
    )

    points = models.IntegerField()
    # unit = models.CharField(max_length=10)  # item / kg
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





    class Meta:
        db_table = 'reward_rules'
        managed = False
        # unique_together = ('category', 'condition')  # same as DB

    def __str__(self):
        return f"{self.category} - {self.condition}"