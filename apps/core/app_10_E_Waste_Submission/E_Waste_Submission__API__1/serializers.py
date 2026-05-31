from rest_framework import serializers
from app_10_E_Waste_Submission.E_Waste_Submission__API__1.models import (
    E_Waste_Submission_Model,
)
from app_3_Recycling_info.models import Recycle_Category
from app_7_Category_Brand_Mapping.models import (
    Category_Brand_Mapping_Model,
    Product_Model_Name_Model,
)
from app_8_Reward_Rules.models import Item_Condition_model
from app_2_e_Facility.models import Facility
from django.utils import timezone
import re
from django.utils.timezone import make_aware
from app_10_E_Waste_Submission.E_Waste_Submission_Images__API__2.models import (
    E_Waste_Submission_Images_Model,
)


# ===============================
# 🔹 MINI SERIALIZERS (ONLY FOR MAPPING)
# ===============================


class Category_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Recycle_Category
        fields = ["id", "title"]  # 👈 only required


class Brand_Mini_Serializer(serializers.ModelSerializer):
    name = serializers.CharField(source="brand.name", read_only=True)

    class Meta:
        model = Category_Brand_Mapping_Model
        fields = ["id", "name"]  # 👈 only required


class Model_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Model_Name_Model
        fields = ["id", "model_name"]  # 👈 only required


class Item_Condition_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Condition_model
        fields = ["id", "display_name"]  # 👈 only required


class Facility_Mini_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "name"]  # 👈 only required


class E_Waste_Submission_Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = E_Waste_Submission_Images_Model
        fields = ["id", "image"]


# ===============================
# 🔹 MAIN MAPPING SERIALIZER
# ===============================


class E_Waste_Submission_Serializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(source='user.first_name + " " + user.last_name', read_only=True)
    # category_name = serializers.CharField(source='category.title', read_only=True)
    # brand_name = serializers.CharField(source='category_brand_mapping.brand.brand_name', read_only=True)
    # model_name = serializers.CharField(source='model.model_name', read_only=True)
    # facility_name = serializers.CharField(source='facility.name', read_only=True)
    # user_condition_name = serializers.CharField(source='user_condition.display_name', read_only=True)
    # final_condition_name = serializers.CharField(source='final_condition.display_name', read_only=True, allow_null=True)
    user_name = serializers.SerializerMethodField()

    # ✅ READ (GET → {} format with name)
    category = Category_Mini_Serializer(read_only=True)
    category_brand_mapping = Brand_Mini_Serializer(read_only=True)
    model = Model_Mini_Serializer(read_only=True)
    user_condition = Item_Condition_Mini_Serializer(read_only=True)
    final_condition = Item_Condition_Mini_Serializer(read_only=True)
    facility = Facility_Mini_Serializer(read_only=True)
    images_data = E_Waste_Submission_Images_Serializer(
        source="images", many=True, read_only=True
    )

    # ✅ WRITE (POST → id pass karo)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Recycle_Category.objects.all(),
        source="category",
        write_only=True,
        error_messages={
            "required": "Please select category",
            "null": "Please select category",
            "does_not_exist": "Invalid category",
            "incorrect_type": "Invalid category id",
        },
    )

    category_brand_mapping_id = serializers.PrimaryKeyRelatedField(
        queryset=Category_Brand_Mapping_Model.objects.all(),
        source="category_brand_mapping",
        write_only=True,
        error_messages={
            "required": "Please select brand",
            "null": "Please select brand",
            "does_not_exist": "Invalid brand",
            "incorrect_type": "Invalid brand id",
        },
    )

    model_id = serializers.PrimaryKeyRelatedField(
        queryset=Product_Model_Name_Model.objects.all(),
        source="model",
        write_only=True,
        error_messages={
            "required": "Please select model",
            "null": "Please select model",
            "does_not_exist": "Invalid model",
            "incorrect_type": "Invalid model id",
        },
    )

    user_condition_id = serializers.PrimaryKeyRelatedField(
        queryset=Item_Condition_model.objects.filter(is_active=True),
        source="user_condition",
        write_only=True,
        error_messages={
            "required": "Please select user condition",
            "null": "Please select user condition",
            "does_not_exist": "Invalid user condition",
            "incorrect_type": "Invalid user condition id",
        },
    )

    final_condition_id = serializers.PrimaryKeyRelatedField(
        queryset=Item_Condition_model.objects.all(),
        source="final_condition",
        # write_only=True,
        required=False,
        allow_null=True,
    )

    facility_id = serializers.PrimaryKeyRelatedField(
        queryset=Facility.objects.all(),
        source="facility",
        write_only=True,
        error_messages={
            "required": "Please select facility",
            "null": "Please select facility",
            "does_not_exist": "Invalid facility",
            "incorrect_type": "Invalid facility id",
        },
    )
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    # images = E_Waste_Submission_Images_Serializer(many=True, read_only=True)

    # ✅ DATE FORMAT (optional but good)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    status = serializers.ChoiceField(
        choices=E_Waste_Submission_Model.STATUS_CHOICES, required=False
    )

    class Meta:
        model = E_Waste_Submission_Model
        fields = [
            "id",
            "user_name",
            "category",
            "category_brand_mapping",
            "model",
            "user_condition",
            "final_condition",
            "facility",
            "user",
            "category_id",
            "category_brand_mapping_id",
            "model_id",
            "user_condition_id",
            "final_condition_id",
            "facility_id",
            "pickup_type",
            "pickup_date",
            "pickup_time",
            "address",
            "phone",
            "notes",
            "images",  # write
            "images_data",  # read
            "weight",
            "status",
            "created_at",
            "updated_at",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ✅ If updating an existing record, images should be optional for Admin
        if self.instance:
            if "images" in self.fields:
                self.fields["images"].required = False

    # Ye method banayein jo dono naam ko jod dega
    def get_user_name(self, obj):
        return (
            f"{obj.user.first_name} {obj.user.last_name}".strip() or obj.user.username
        )

    # ====================== WRITE FIELDS ======================

    pickup_type = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Pickup type is required",
            "blank": "Pickup type cannot be empty",
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

    pickup_date = serializers.DateField(
        required=True,
        error_messages={
            "required": "Pickup date is required",
        },
    )

    pickup_time = serializers.TimeField(
        required=True,
        error_messages={
            "required": "Pickup time is required",
        },
    )

    phone = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Phone is required",
            "blank": "Phone cannot be empty",
            "invalid": "Phone must contain only numbers",
            "max_length": "Phone cannot be more than 10 digits",
            "min_length": "Phone cannot be less than 10 digits",
        },
    )

    notes = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "Notes is required",
            "blank": "Notes cannot be empty",
        },
    )

    # ====================== Validation ======================
    def validate_phone(self, value):
        if not re.fullmatch(r"^[0-9]{10}$", value):
            raise serializers.ValidationError("Phone must be exactly 10 digits")
        return value

    def validate_pickup_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Pickup date cannot be in the past")
        return value

    def validate_pickup_type(self, value):
        if value not in ["pickup", "dropoff"]:
            raise serializers.ValidationError("Invalid pickup type")
        return value

    def validate_address(self, value):
        if not value:
            raise serializers.ValidationError("Address is required")
        return value

    def validate_notes(self, value):
        if not value:
            raise serializers.ValidationError("Notes is required")
        return value

    def validate(self, data):
        pickup_date = data.get("pickup_date")
        pickup_time = data.get("pickup_time")

        now = timezone.now()

        if pickup_date and pickup_time:
            naive_datetime = timezone.datetime.combine(pickup_date, pickup_time)
            pickup_datetime = make_aware(naive_datetime)

            if pickup_datetime < now:
                raise serializers.ValidationError(
                    {"pickup_time": "Pickup date & time cannot be in the past"}
                )

        category = data.get("category")
        mapping = data.get("category_brand_mapping")
        model = data.get("model")

        if mapping and category:
            if mapping.category_id != category.id:
                raise serializers.ValidationError(
                    {
                        "category_brand_mapping_id": "Selected brand does not belong to selected category"
                    }
                )

        if model and mapping:
            if model.brand_id != mapping.brand_id:
                raise serializers.ValidationError(
                    {"model_id": "Selected model does not belong to selected brand"}
                )

        return data

    # -------------------------------------------------------
    # ============================ CREATE ============================
    # -------------------------------------------------------
    def create(self, validated_data):
        from django.db import transaction

        # 🔥 FORCE DEFAULT STATUS
        validated_data["status"] = "requested"

        images = validated_data.pop("images", [])

        if not images:
            raise serializers.ValidationError(
                {"images": "Minimum 3 images are required for new submission"}
            )

        with transaction.atomic():
            submission = E_Waste_Submission_Model.objects.create(**validated_data)

            for img in images:
                E_Waste_Submission_Images_Model.objects.create(
                    submission=submission, image=img
                )

        return submission

    # -------------------------------------------------------
    # ============================ UPDATE ============================
    # -------------------------------------------------------
    def update(self, instance, validated_data):
        from django.db import transaction

        # ✅ Admin can ONLY update these 3 fields for verification
        allowed_fields = ["final_condition", "status", "weight"]

        with transaction.atomic():
            # Update only specific fields
            for attr in allowed_fields:
                if attr in validated_data:
                    setattr(instance, attr, validated_data[attr])

            instance.save()

        return instance

    def validate_status(self, value):
        """
        🔥 Status Sequence & Duplicate Validation Logic
        Since status is updated via Submission API, logic must be here.
        """
        # We only validate during UPDATE (when instance exists)
        if self.instance:
            current_status = self.instance.status

            # ✅ IMPORTANT FIX
            # Agar status change hi nahi ho raha → skip validation
            if value == current_status:
                return value
                
            new_status = value

            # Standard linear flow
            STATUS_FLOW = [
                "requested",
                "picked_up_dropped_off",
                "evaluating",
                "recycled",
                "rewarded"
            ]

            # 1. Duplicate check
            if new_status == current_status:
                raise serializers.ValidationError(
                    f"Status is already set to '{current_status}'. No change detected."
                )

            # 2. Terminal State check: Once rewarded or rejected, no further changes
            # Cannot change status. This submission is already 'rewarded'
            if current_status in ["rewarded", "rejected"]:
                raise serializers.ValidationError(
                    f"Cannot change status. This submission is already '{current_status}' (Terminal State)."
                )

            # 3. Special case: 'rejected' is allowed from any non-terminal state
            if new_status == "rejected":
                return value

            # 4. Sequence check for standard flow
            try:
                # If current status isn't in standard flow (shouldn't happen, but safe check)
                if current_status not in STATUS_FLOW:
                    raise serializers.ValidationError(
                        f"Current status '{current_status}' cannot transition to '{new_status}'."
                    )

                current_index = STATUS_FLOW.index(current_status)
                
                # Check if new status is also in the flow
                if new_status not in STATUS_FLOW:
                    raise serializers.ValidationError(f"'{new_status}' is not a valid status.")
                
                new_index = STATUS_FLOW.index(new_status)

                # Enforce strictly one-step-at-a-time transition
                if new_index != current_index + 1:
                    expected_next = STATUS_FLOW[current_index + 1]
                    raise serializers.ValidationError(
                        f"Invalid Sequence! From '{current_status}', the only allowed next step is '{expected_next}'."
                    )
            except (ValueError, IndexError):
                raise serializers.ValidationError(
                    f"Invalid status transition logic from '{current_status}' to '{new_status}'."
                )

        return value

    def validate_images(self, images):
        if images is not None:
            if len(images) < 3:
                raise serializers.ValidationError("Minimum 3 images required")
            if len(images) > 5:
                raise serializers.ValidationError("Maximum 5 images allowed")
        return images
