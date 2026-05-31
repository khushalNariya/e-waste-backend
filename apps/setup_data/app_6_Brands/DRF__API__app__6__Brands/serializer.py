from rest_framework import serializers
from app_6_Brands.models import Brand


from rest_framework import serializers
# from .models import Brand, CategoryBrandMapping

# Brand Serializer


class Brand_Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d %b %Y, %I:%M %p",
        read_only=True
    )

    updated_at = serializers.DateTimeField(
        format="%d %b %Y, %I:%M %p",
        read_only=True
    )

    class Meta:
        model = Brand
        fields = ["id",
                    "name",
                    "created_at",
                    "updated_at"
        ]

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Brand name too short")
        return value
