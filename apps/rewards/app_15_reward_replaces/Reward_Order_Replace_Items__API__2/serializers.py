from rest_framework import serializers
from django.contrib.auth.models import User
from app_15_reward_replaces.Reward_Order_Replace_Items__API__2.models import Reward_Order_Replace_Item


# Serializer for replace items — read-only admin view
class Reward_Order_Replace_Item_Serializer(serializers.ModelSerializer):
    replace_number = serializers.CharField(source='replace_request.replace_number', read_only=True)
    order_number   = serializers.CharField(source='replace_request.order.order_number', read_only=True)

    class Meta:
        model  = Reward_Order_Replace_Item
        fields = [
            'id',
            'replace_request',
            'replace_number',
            'order_number',
            'order_item',
            'product',
            'product_name',
            'quantity',
            'points',
            'subtotal_points',
            'item_condition',
            'replacement_product',
            'replacement_product_name',
        ]
