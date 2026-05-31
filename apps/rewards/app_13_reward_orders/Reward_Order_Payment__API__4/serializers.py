from rest_framework import serializers
from .models import Reward_Order_Payment

# ==========================================
# ORDER PAYMENT SERIALIZER
# ==========================================
class Reward_Order_Payment_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Reward_Order_Payment
        fields = "__all__"
