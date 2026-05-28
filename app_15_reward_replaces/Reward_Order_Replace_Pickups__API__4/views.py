from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from app_15_reward_replaces.Reward_Order_Replace_Pickups__API__4.models import Reward_Order_Replace_Pickup
from app_15_reward_replaces.Reward_Order_Replace_Pickups__API__4.serializers import Reward_Order_Replace_Pickup_Serializer
from app_15_reward_replaces.Pagination__File.pagination import RewardReplace_Pagination


# =============================================================
# ADMIN REPLACE PICKUPS VIEWSET (Read Only)
# Admin can list and view courier pickup + delivery tracking info.
# Pickup records are auto-created when replace request is submitted.
# Pickup status updates happen automatically via the main request viewset.
# =============================================================
class Admin_Reward_Order_Replace_Pickup_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = Reward_Order_Replace_Pickup.objects.all().order_by("-id")
    serializer_class   = Reward_Order_Replace_Pickup_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class   = RewardReplace_Pagination

    filter_backends  = [DjangoFilterBackend, filters.SearchFilter]
    search_fields    = [
        "replace_request__replace_number",
        "replace_request__order__order_number",
        "order_address__full_name",
        "order_address__phone",
        "tracking_number",
    ]
    filterset_fields = ["pickup_status", "replace_request"]
