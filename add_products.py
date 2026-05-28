# import os
# import sys
# import django
# from django.core.files import File

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_waste_recycling.settings')
# django.setup()

# from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model
# from app_9_Reward_Products.Reward_Category__API__1.models import Reward_Category_model
# from app_9_Reward_Products.Reward_Product_Images__API__3.models import Reward_Product_Image_model

# # Ensure at least one category exists
# cat, created = Reward_Category_model.objects.get_or_create(
#     name="Eco Products",
#     defaults={'slug': 'Eco-Products', 'is_active': True}
# )

# # Product 1
# p1 = Reward_Product_model.objects.create(
#     name="Eco-Friendly Bamboo Coffee Cup",
#     category=cat,
#     points=500,
#     stock=100,
#     description="Reusable bamboo coffee cup to reduce plastic waste.",
#     terms="Can be redeemed once per month.",
#     tag="Popular",
#     delivery_days="3-5",
#     rating=4.8,
#     is_active=True
# )

# # Product 2
# p2 = Reward_Product_model.objects.create(
#     name="Recycled Plastic Laptop Sleeve",
#     category=cat,
#     points=1200,
#     stock=50,
#     description="Sleek modern laptop sleeve made from recycled ocean plastics.",
#     terms="Non-refundable.",
#     tag="Premium",
#     delivery_days="5-7",
#     rating=4.9,
#     is_active=True
# )

# # Attach images
# img1_path = r"C:\Users\KHUSHAL\.gemini\antigravity\brain\30f863a8-7159-4d40-b5d6-cc26c1f90d8c\bamboo_coffee_cup_1777557482799.png"
# with open(img1_path, 'rb') as f:
#     Reward_Product_Image_model.objects.create(
#         product=p1,
#         image=File(f, name='bamboo_coffee_cup.png'),
#         is_primary=True,
#         display_order=1,
#         is_active=True
#     )

# img2_path = r"C:\Users\KHUSHAL\.gemini\antigravity\brain\30f863a8-7159-4d40-b5d6-cc26c1f90d8c\recycled_laptop_sleeve_1777557499312.png"
# with open(img2_path, 'rb') as f:
#     Reward_Product_Image_model.objects.create(
#         product=p2,
#         image=File(f, name='recycled_laptop_sleeve.png'),
#         is_primary=True,
#         display_order=1,
#         is_active=True
#     )

# print("Successfully added 2 products and their images!")
