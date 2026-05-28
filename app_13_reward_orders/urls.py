from django.urls import path
from .Reward_Order__API__1.views import User_Reward_Order_ViewSet
from .Reward_Order_Address__API__3.views import User_Reward_Order_Address_ViewSet
from .Reward_Order_Status_History__API__5.views import User_Reward_Order_Status_History_ViewSet

urlpatterns = [
    # =========================
    # User URLS
    # =========================
    path(
        "reward-orders/", 
        User_Reward_Order_ViewSet.as_view({"get": "list"})
    ),
    path(
        "checkout/", 
        User_Reward_Order_ViewSet.as_view({"post": "checkout"})
    ),
    path(
        "cancel-order/", 
        User_Reward_Order_ViewSet.as_view({"post": "cancel_order"})
    ),
    path(
        "reward-order-address/", 
        User_Reward_Order_Address_ViewSet.as_view({"get": "list", "post": "create"})
    ),
    path(
        "reward-order-address/<int:pk>/", 
        User_Reward_Order_Address_ViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})
    ),
    path(
        "reward-order-history/", 
        User_Reward_Order_Status_History_ViewSet.as_view({"get": "list"})
    ),


    # =========================
]
