from django.urls import path
from app_9_Reward_Products.Reward_Category__API__1.views import (
    Reward_Category_ViewSet, Reward_Category_User_ViewSet
)
from app_9_Reward_Products.Reward_Product__API__2.views import (
    Reward_Product_ViewSet, Reward_Product_User_ViewSet
)


urlpatterns = [
    path("reward-category/", Reward_Category_User_ViewSet.as_view({"get": "list"})),
    path("reward-category/<int:pk>/", Reward_Category_ViewSet.as_view({"get": "retrieve"})),

    path("reward-product/", Reward_Product_User_ViewSet.as_view({"get": "list"})),
    path("reward-product/<slug:slug>/", Reward_Product_User_ViewSet.as_view({"get": "retrieve"})),
]
