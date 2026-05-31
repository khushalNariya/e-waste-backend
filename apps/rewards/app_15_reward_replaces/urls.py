from django.urls import path
from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.views import User_Reward_Order_Replace_Request_ViewSet
from app_15_reward_replaces.Reward_Order_Replace_Status_History__API__3.views import User_Reward_Order_Replace_Status_History_ViewSet

urlpatterns = [
    # =========================
    # User-Side URLs
    # =========================

    # List own replace requests + submit new replace request
    path(
        "reward-replaces/",
        User_Reward_Order_Replace_Request_ViewSet.as_view({"get": "list", "post": "create"})
    ),
    # View detail of a single replace request
    path(
        "reward-replaces/<int:pk>/",
        User_Reward_Order_Replace_Request_ViewSet.as_view({"get": "retrieve"})
    ),
    path(
        "reward-replaces/<int:pk>/cancel/",
        User_Reward_Order_Replace_Request_ViewSet.as_view({"post": "cancel"})
    ),
    # View status history for own replace requests
    path(
        "reward-replaces-history/",
        User_Reward_Order_Replace_Status_History_ViewSet.as_view({"get": "list"})
    ),
]
