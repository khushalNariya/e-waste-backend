from django.db import models
from app_6_Brands.models import Brand  # Important
from app_3_Recycling_info.models import Recycle_Category  # Important

class Category_Brand_Mapping_Model(models.Model):
    category = models.ForeignKey(Recycle_Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category_brand_mapping"
        # unique_together = ('category', 'brand')
        managed = False

    def __str__(self):
        return f"{self.category} - {self.brand}"


# ========================================================================
# ================ Product (Wise) Model Name (e.g., iPhone X, Galaxy S21,vivo v20,oppo f30,Samsung M30,LG G8) ================================
# ========================================================================
class Product_Model_Name_Model(models.Model):
    category = models.ForeignKey(Recycle_Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    model_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product_model_name"
        managed = False

    def __str__(self):
        return f"{self.brand} - {self.model_name}"


