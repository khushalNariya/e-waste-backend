from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils import timezone
from app_1_users.models import UserProfile
from datetime import datetime
from django.utils.timezone import make_aware

from rest_framework_simplejwt.tokens import RefreshToken


# =================================================
# 1️⃣ REGISTER SERIALIZER (POST ONLY)
# =================================================
class BaseUserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "First name cannot be empty",
            "blank": "First name cannot be Empty"
        }
    )


    last_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Last name cannot be empty",
            "blank": "Last name cannot be Empty"
        }
    )



    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Email is required",
            "blank": "Email cannot be Empty"
        }
    )

    mobile_number = serializers.CharField(
    required=True,
    allow_blank=False,
        write_only=True,

    error_messages={
        "required": "Mobile number is required",
        "blank": "Mobile number cannot be Empty"
    }
)

    address_line_1 = serializers.CharField(
        required=True,
        allow_blank=False,
            write_only=True,

        error_messages={
            "required": "Address Line 1 is required",
            "blank": "Address Line 1 cannot be Empty"
        }
    )

    address_line_2 = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True
    )
    
    city = serializers.CharField(
        required=True,
        allow_blank=False,
            write_only=True,

        error_messages={
            "required": "City cannot be blank",
            "blank": "City cannot be Empty"
        }
    )
    

    pincode = serializers.CharField(
        required=True,
        allow_blank=False,
            write_only=True,

        error_messages={
            "required": "Pincode is required",
            "blank": "Pincode cannot be Empty"
        }
    )

    state = serializers.CharField(
        required=True,
        allow_blank=False,
            write_only=True,

        error_messages={
            "required": "State cannot be blank",
            "blank": "State cannot be Empty"
        }
    )

    password = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Password cannot be empty",
            "blank": "Password cannot be Empty"
        }
    )

    confirmPassword = serializers.CharField(
        # required=True,
        # allow_blank=False,
        write_only=True,
        error_messages={
            "required": "ConfirmPassword cannot be empty",
            "blank": "Please Enter Confirm Password"
        }
    )

    # ---- extra fields (UserProfile ke liye) ----
       
    # confirmPassword = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'confirmPassword',  # ✅ ADD THIS

            # extra inputs
            'mobile_number',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'pincode',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'show_password':{'write_only':True}
        }

    # -------- VALIDATIONS --------
    # def validate_first_name(self, value):
    #     if not value.strip():
    #         raise serializers.ValidationError("First name cannot be empty")
    #     return value

    # def validate_last_name(self, value):
    #     if not value.strip():
    #         raise serializers.ValidationError("Last name cannot be empty")
    #     return value

    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("Email already registered")
    #     return value
    
    def validate_email(self, value):
        user = getattr(self, 'instance', None)  # instance exists in update
        qs = User.objects.exclude(pk=user.pk) if user else User.objects.all()
        if qs.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered")
        return value
    
    def validate_mobile_number(self, value):
        # if not value.strip():
        #     raise serializers.ValidationError("Mobile number cannot be empty")
        if not value.isdigit():
            raise serializers.ValidationError("Mobile number must contain only digits")
        if len(value) != 10:           
            raise serializers.ValidationError("Mobile number must be at least 10 digits")
        return value
    
    def validate_pincode(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Pincode must contain only digits")
        if len(value) != 6:
            raise serializers.ValidationError("Pincode must be exactly 6 digits")
        return value


    def validate_address_line_1(self, value):
        if not value.strip():
            raise serializers.ValidationError("Address Line 1 cannot be empty")
        return value


    def validate_state(self, value):
        if not value.strip():
            raise serializers.ValidationError("State cannot be blank")
        return value
    
    def validate(self, data):
        print("DATA RECEIVED:", data)

        # -------------- trim (White-Space) Remove
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        # --------- Password (Field) Validation
        if data.get("password") != data.get("confirmPassword"):
            raise serializers.ValidationError({
                "confirmPassword": ["Passwords do Not match"]
            })
        return data
    
    # def validate_city(self, value):
    #     if not value.strip():
    #         raise serializers.ValidationError("City cannot be blank")
    #     return value

    # def validate_state(self, value):
    #     if not value.strip():
    #         raise serializers.ValidationError("State cannot be blank")
    #     return value
    

    # -------- CREATE --------
class RegisterSerializer(BaseUserSerializer):
    def create(self, validated_data):

        validated_data.pop("confirmPassword")  # remove confirm password

        # profile fields alag kiye
        profile_data = {
            'mobile_number': validated_data.pop('mobile_number'),
            'address_line_1': validated_data.pop('address_line_1'),
            'address_line_2': validated_data.pop('address_line_2', ''),
            'city': validated_data.pop('city'),
            'state': validated_data.pop('state'),
            'pincode': validated_data.pop('pincode'),
        }

        # auto username
        # username = f"user{User.objects.count() + 1}"
        
        # Auto-generate username based on last user ID
        last_user = User.objects.order_by('-id').first()
        next_id = last_user.id + 1 if last_user else 1
        username_1 = f"user{next_id}"
        
        raw_password = validated_data['password']

        # auth_user (password HASH hoga)
        user_2 = User.objects.create_user(
            username=username_1,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=raw_password
        )

        fixed_updated_time = make_aware(datetime(1970, 1, 1, 5, 30, 0))  # timezone aware

        # UserProfile create
        UserProfile.objects.create(
            user_1=user_2,
            Show_Password=raw_password,  # plain password save
            user_created_on=timezone.now(),
            # user_updated_on=timezone.now(),
            user_updated_on=fixed_updated_time,  # fixed old timestamp

            **profile_data
        )

        return user_2



class UpdateUserSerializer(BaseUserSerializer):
    def update(self, instance, validated_data):
        profile_data = {
            'mobile_number': validated_data.pop('mobile_number', None),
            'address_line_1': validated_data.pop('address_line_1', None),
            'address_line_2': validated_data.pop('address_line_2', None),
            'city': validated_data.pop('city', None),
            'state': validated_data.pop('state', None),
            'pincode': validated_data.pop('pincode', None),
        }

        # User update
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        instance.save()

        # UserProfile update
        profile = UserProfile.objects.get(user_1=instance)
        for key, value in profile_data.items():
            if value is not None:
                setattr(profile, key, value)
        if validated_data.get('password'):
            profile.Show_Password = validated_data['password']

        profile.user_updated_on = timezone.now()
        
        profile.save()

        return instance


# =================================================
# 2️⃣ USER PROFILE SERIALIZER (GET)
# =================================================
class UserProfileSerializer(serializers.ModelSerializer):

    user_created_on = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    user_updated_on = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
        
    class Meta:
        model = UserProfile
        fields = [
            'Show_Password',
            'mobile_number',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'pincode',
            'user_created_on',
            'user_updated_on',
        ]


# =================================================
# 3️⃣ USER DETAIL SERIALIZER (GET)
# =================================================
class UserDetailSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
        ]



# ================================ Login ===================================

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            raise serializers.ValidationError({"non_field_errors": ["Invalid credentials"]})

        # JWT Token
        refresh = RefreshToken.for_user(user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user_id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
            "is_active":user.is_active
        }
