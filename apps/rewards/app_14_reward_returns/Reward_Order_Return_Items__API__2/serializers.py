from rest_framework import serializers
from .models import Reward_Order_Return_Item

# Serializer for return items - Read Only for Admin dashboard representation
class Reward_Order_Return_Item_Serializer(serializers.ModelSerializer):
    return_number = serializers.CharField(source='return_request.return_number', read_only=True)
    order_number = serializers.CharField(source='return_request.order.order_number', read_only=True)

    class Meta:
        model = Reward_Order_Return_Item
        fields = [
            'id',
            'return_request',
            'return_number',
            'order_number',
            'order_item',
            'product',
            'product_name',
            'quantity',
            'points',
            'subtotal_points',
            'item_condition'
        ]
