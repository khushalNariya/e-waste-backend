from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from .models import Reward_Order_Return_Item
from .serializers import Reward_Order_Return_Item_Serializer
from app_14_reward_returns.Pagination__File.pagination import RewardReturn_Pagination

# =========================================================
# ADMIN RETURN ITEMS VIEWSET (READ ONLY FOR ADMIN DASHBOARD)
# Allows listing and retrieving return items without modification.
# =========================================================
class Admin_Reward_Order_Return_Item_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reward_Order_Return_Item.objects.all().order_by("-id")
    serializer_class = Reward_Order_Return_Item_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = RewardReturn_Pagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["product_name", "return_request__return_number", "return_request__order__order_number"]
    filterset_fields = ["return_request"]
