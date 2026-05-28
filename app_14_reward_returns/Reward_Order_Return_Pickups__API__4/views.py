from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from .models import Reward_Order_Return_Pickup
from .serializers import Reward_Order_Return_Pickup_Serializer
from app_14_reward_returns.Pagination__File.pagination import RewardReturn_Pagination

# =========================================================
# ADMIN RETURN PICKUPS VIEWSET (READ ONLY FOR ADMIN DASHBOARD)
# Allows listing and retrieving courier pickup schedules.
# =========================================================
class Admin_Reward_Order_Return_Pickup_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reward_Order_Return_Pickup.objects.all().order_by("-id")
    serializer_class = Reward_Order_Return_Pickup_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = RewardReturn_Pagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["return_request__return_number", "return_request__order__order_number", "order_address__full_name", "order_address__phone"]
    filterset_fields = ["pickup_status", "return_request"]
