from rest_framework import serializers
from .models import Reward_Order_Address
from django.core.validators import RegexValidator

# ==========================================
# ORDER ADDRESS SERIALIZER
# ==========================================
class Reward_Order_Address_Serializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Full name is required",
            "blank": "Full name cannot be empty",
        },
    )
    phone = serializers.CharField(
        required=True,
        allow_blank=False,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Phone number must be exactly 10 digits",
            )
        ],
        error_messages={
            "required": "Phone number is required",
            "blank": "Phone number cannot be empty",
        },
    )
    address = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Address is required",
            "blank": "Address cannot be empty",
        },
    )
    city = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "City is required",
            "blank": "City cannot be empty",
        },
    )
    state = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "State is required",
            "blank": "State cannot be empty",
        },
    )
    pincode = serializers.CharField(
        required=True,
        allow_blank=False,
        validators=[
            RegexValidator(
                regex=r'^\d{6}$',
                message="Pincode must be exactly 6 digits",
            )
        ],
        error_messages={
            "required": "Pincode is required",
            "blank": "Pincode cannot be empty",
        },
    )

    class Meta:
        model = Reward_Order_Address
        fields = "__all__"
        extra_kwargs = {
            'order': {'required': False}
        }
