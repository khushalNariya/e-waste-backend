from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .User_Rewards__API__1.views import User_Wallet_User_ViewSet, Reward_Transaction_User_ViewSet

router = DefaultRouter()
router.register(r'wallet', User_Wallet_User_ViewSet, basename='user-wallet')
router.register(r'transactions', Reward_Transaction_User_ViewSet, basename='reward-transactions')

urlpatterns = [
    path('', include(router.urls)),
]
