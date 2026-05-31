from rest_framework import serializers
from .models import Reward_Order_Item
from app_9_Reward_Products.Reward_Product_Images__API__3.models import Reward_Product_Image_model

class Reward_Order_Item_Serializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Reward_Order_Item
        fields = [
            "id",
            "order",
            "product_id",
            "product_name",
            "quantity",
            "points",
            "subtotal_points",
            "created_at",
            "image",
        ]

    def get_image(self, obj):
        try:
            # Query the primary image of this product
            img = Reward_Product_Image_model.objects.filter(product_id=obj.product_id, is_primary=True).first()
            if not img:
                # If no primary image is set, try to get the first available image
                img = Reward_Product_Image_model.objects.filter(product_id=obj.product_id).first()
            
            if img and img.image:
                request = self.context.get('request')
                if request:
                    return request.build_absolute_uri(img.image.url)
                return img.image.url
        except Exception as e:
            pass
        return None
