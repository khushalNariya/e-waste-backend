from rest_framework import serializers
from app_4_Education.models import EducationArticle_model
import os

class Education_Serializer(serializers.ModelSerializer):
    Education_Create_at = serializers.DateTimeField(
    format="%d %b %Y, %I:%M %p",
        read_only=True
    )

    Education_Update_at = serializers.DateTimeField(
    format="%d %b %Y, %I:%M %p",
        read_only=True
    )

    # ================= FIELD VALIDATION =================

    title = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Title cannot be empty",
            "blank": "Title cannot be empty"
        }
    )

    description = serializers.CharField(
            required=True,
            allow_blank=False,
            error_messages={
                "required": "Description is required",
                "blank": "Description cannot be empty"
            }
        )

    image = serializers.ImageField(
        required=True,
        # allow_blank=False,
        error_messages={
            "required": "Image is required",
            "blank": "Image cannot be empty"
        }
    )

    category = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Category is required",
            "blank": "Category cannot be empty"
        }
    )

    author = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Author name is required",
            "blank": "Author cannot be empty"
        }
    )

    date = serializers.DateField(
        required=True,
        error_messages={
            "required": "Date is required",
            "invalid": "Invalid date format (YYYY-MM-DD)"
        }
    )

    readTime = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Read Time is required",
            "blank": "Read Time cannot be empty"
        }
    )

    isFeatured = serializers.BooleanField(required=False)
        
    class Meta:
        model = EducationArticle_model
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
        extra_kwargs = {
                "image": {"use_url": True}
            }

    # ================= COMMON VALIDATION =================
    def validate(self, data):

        """
        Step 1: Trim all string fields (remove spaces)
        Step 2: Check image required on create only
        """

        # TRIM ALL FIELDS
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        # IMAGE REQUIRED ONLY ON CREATE (Only allow image on create request)
        if not self.instance:
            if not data.get("image"):
                raise serializers.ValidationError({
                    "image": "Image is required."
                })
        return data


    # ================= TITLE UNIQUE (CASE-INSENSITIVE) =================
    def validate_title(self, value):
        """
        Prevent duplicate titles (case-insensitive)
        Allow same value during edit
        """

        value = value.strip()

        qs = EducationArticle_model.objects.filter(title__iexact=value)

        # ✅ IMPORTANT: Exclude current record (for edit)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError("Title already exists")

        return value
    

    # ================= IMAGE UPDATE =================

    def update(self, instance, validated_data):

        """
        If new image uploaded → delete old image
        """

        new_image = validated_data.get("image", None)

        # Agar new image aa rahi hai
        if new_image:
            # Old image exist karti hai?
            if instance.image and os.path.isfile(instance.image.path):
                os.remove(instance.image.path)

        return super().update(instance, validated_data)