from rest_framework import serializers
from app_3_Recycling_info.models import Recycle_Category




class Recycle_Serializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d %b %Y, %I:%M %p",
        read_only=True
    )

    updated_at = serializers.DateTimeField(
        format="%d %b %Y, %I:%M %p",
        read_only=True
    )


    title = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Title cannot be empty",
            "blank": "Title cannot be Empty"
        }
    )

    description = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Description cannot be empty",
            "blank": "Description cannot be Empty"
        }
    )

    process = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Process cannot be empty",
            "blank": "Process cannot be Empty"
        }
    )

    instruction = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Instruction cannot be empty",
            "blank": "Instruction cannot be Empty"
        }
    )

    benefits = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Benefits cannot be empty",
            "blank": "Benefits cannot be Empty"
        }
    )

    button_text = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Button text cannot be empty",
            "blank": "Button text cannot be Empty"
        }
    )

    icon = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Icon cannot be empty",
            "blank": "Icon cannot be Empty"
        }
    )

# =================== .Strim (White-Space) Remove ============================
    def validate(self, data):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data

# =================== Validations ============================

    def validate_title(self, value):
        value = value.strip() # Remove leading/trailing whitespace

        qs = Recycle_Category.objects.filter(title__iexact=value) # same title (case-insensitive)

        # 🔥 agar edit hai to current record exclude karo
        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError("Title already exists")

        return value

# ======================= Process (Field) Validation ============================
    def validate_process(self, value):
        steps = [s.strip() for s in value.split("\n") if s.strip()]
        return " → ".join(steps)
    

# Serializer setting / configuration section
    class Meta:
        model = Recycle_Category  # This tells Django which model this serializer is connected to
        fields = '__all__'  # This tells Django which model this serializer is connected to
