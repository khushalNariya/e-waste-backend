from rest_framework import serializers
from .models import User_Wallet_Model, Reward_Transaction_Model

# ===============================
# 🔹 MINI SERIALIZERS (ONLY FOR MAPPING)
# ===============================


# class Recycle_Category_MiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recycle_Category
#         fields = ["id", "title"]  # 👈 only required


# ===============================
# 🔹 USER WALLET SERIALIZER
# ===============================
class User_Wallet_Serializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.get_full_name", read_only=True)
    # ✅ DATE FORMAT (optional but good)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    class Meta:
        model = User_Wallet_Model
        fields = ["id", "user", "user_name", "total_points", "created_at", "updated_at"]


# ===============================
# 🔹 REWARD TRANSACTION SERIALIZER
# ===============================
class Reward_Transaction_Serializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.get_full_name", read_only=True)
    # ✅ DATE FORMAT (optional but good)
    created_at = serializers.DateTimeField(format="%d %b %Y, %I:%M %p", read_only=True)

    class Meta:
        model = Reward_Transaction_Model
        fields = [
            "id",
            "user",
            "user_name",
            "submission",
            "order",
            "points",
            "type",
            "description",
            "created_at",
        ]
