from django.urls import path
from app_14_reward_returns.Reward_Order_Return_Request__API__1.views import User_Reward_Order_Return_Request_ViewSet
from app_14_reward_returns.Reward_Order_Return_Status_History__API__3.views import User_Reward_Order_Return_Status_History_ViewSet

urlpatterns = [
    # =========================
    # User-Side URLs
    # =========================
    path(
        "reward-returns/", 
        User_Reward_Order_Return_Request_ViewSet.as_view({"get": "list", "post": "create"})
    ),
    path(
        "reward-returns/<int:pk>/", 
        User_Reward_Order_Return_Request_ViewSet.as_view({"get": "retrieve"})
    ),
    path(
        "reward-returns/<int:pk>/cancel/", 
        User_Reward_Order_Return_Request_ViewSet.as_view({"post": "cancel"})
    ),
    path(
        "reward-returns-history/", 
        User_Reward_Order_Return_Status_History_ViewSet.as_view({"get": "list"})
    ),
]
