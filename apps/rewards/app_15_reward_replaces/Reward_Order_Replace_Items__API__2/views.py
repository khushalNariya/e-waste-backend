from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from app_15_reward_replaces.Reward_Order_Replace_Items__API__2.models import Reward_Order_Replace_Item
from app_15_reward_replaces.Reward_Order_Replace_Items__API__2.serializers import Reward_Order_Replace_Item_Serializer
from app_15_reward_replaces.Pagination__File.pagination import RewardReplace_Pagination


# =============================================================
# ADMIN REPLACE ITEMS VIEWSET (Read Only)
# Admin can list and view individual items of a replace request.
# Items are auto-created during replace request submission.
# =============================================================
class Admin_Reward_Order_Replace_Item_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = Reward_Order_Replace_Item.objects.all().order_by("-id")
    serializer_class   = Reward_Order_Replace_Item_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class   = RewardReplace_Pagination

    filter_backends  = [DjangoFilterBackend, filters.SearchFilter]
    search_fields    = ["product_name", "replace_request__replace_number", "replace_request__order__order_number"]
    filterset_fields = ["replace_request"]
