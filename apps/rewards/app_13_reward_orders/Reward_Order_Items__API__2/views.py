from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Reward_Order_Item
from .serializers import Reward_Order_Item_Serializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from app_13_reward_orders.Pagination__File.pagination import user__Pagination

# =========================================================
# ADMIN ORDER ITEM API
# =========================================================
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class Admin_Reward_Order_Item_ViewSet(viewsets.ModelViewSet):

    queryset = Reward_Order_Item.objects.all().order_by("-id")
    serializer_class = Reward_Order_Item_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = user__Pagination
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["product_name", "order__order_number"]
    filterset_fields = ["order"]
