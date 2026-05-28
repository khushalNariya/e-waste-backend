from app_7_Category_Brand_Mapping.models import Product_Model_Name_Model
from rest_framework import serializers
from .models import E_Waste_Status_History_Model
from django.contrib.auth.models import User

# Serializer to show small user info (ID and Name)
class User_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]

# Serializer to show product details (Name, Category, Brand)
class Product_Mini_Serializer(serializers.ModelSerializer):
    # Mapping 'model_name' from DB to 'name' in JSON
    name = serializers.CharField(source="model_name")
    # Fetching 'title' from the related category
    category = serializers.CharField(source="category.title")
    # Fetching 'name' from the related brand
    brand = serializers.CharField(source="brand.name")

    class Meta:
        model = Product_Model_Name_Model
        fields = ["id", "name", "category", "brand"]

# Main serializer for E-Waste Status History
class E_Waste_Status_History_Serializer(serializers.ModelSerializer):
    # Getting product info from the related submission's model
    product = Product_Mini_Serializer(source="submission.model", read_only=True)
    # Getting user info who made the submission
    user = User_Mini_Serializer(source="submission.user", read_only=True)
    # User who changed the status (Admin/Staff)
    changed_by = User_Mini_Serializer(read_only=True)

    # Field to show the first image of the submission
    image = serializers.SerializerMethodField()

    # Custom date format (e.g., 17 Apr 2026, 11:20 PM)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    # Using created_at as updated_at since the history record doesn't change
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True, source="created_at")

    class Meta:
        model = E_Waste_Status_History_Model
        fields = [
            "id",
            "submission",
            "product",
            "user",
            "image",
            "status",
            "remarks",
            "changed_by",
            "created_at",
            "updated_at",
        ]

    # Function to get the absolute URL of the submission image
    def get_image(self, obj):
        request = self.context.get("request")
        # Get the first image linked to the submission
        first_image = obj.submission.images.first()
        if first_image and first_image.image:
            return request.build_absolute_uri(first_image.image.url)
        return None