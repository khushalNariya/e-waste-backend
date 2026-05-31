from rest_framework.viewsets import ModelViewSet
from app_8_Reward_Rules.models import Item_Condition_model
from .serializer import Item_Condition_Serializer
from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.authentication import SessionAuthentication

# --- Pagination
from .pagination import user__Pagination  # ---- import (pagination.py) file
from rest_framework.permissions import IsAdminUser,IsAuthenticated

# ===========================================================================
# ======================== Item Condition (Admin) Interface ========================
# ===========================================================================
class Item_Condition_ViewSet(ModelViewSet):
    queryset = Item_Condition_model.objects.all()
    serializer_class = Item_Condition_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser] # is_staf = true, is_active = true

# ---------- Combine All Filters -----------
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "name",
        "display_name",
    ]

    pagination_class = user__Pagination  # ---- import (pagination.py) file

