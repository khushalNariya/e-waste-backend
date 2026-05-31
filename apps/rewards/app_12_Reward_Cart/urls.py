from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .Reward_Cart__API__1.views import User_Reward_Cart_ViewSet
from .Reward_Cart_Items__API__2.views import User_Reward_Cart_Items_ViewSet

# Create Router for User Side
router = DefaultRouter()
router.register("cart", User_Reward_Cart_ViewSet, basename="user_cart")
router.register("cart-items", User_Reward_Cart_Items_ViewSet, basename="user_cart_items")

urlpatterns = [
    path("", include(router.urls)),
]
