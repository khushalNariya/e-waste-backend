from rest_framework.viewsets import ModelViewSet
from .models import Reward_Category_model
from .serializer import Reward_Category_Serializer
from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.authentication import SessionAuthentication

# --- Pagination
from ..Pagination__File.pagination import user__Pagination  # ---- import (pagination.py) file
from rest_framework.permissions import IsAdminUser, IsAuthenticated


# ===========================================================================
# ======================== Reward Category (Admin) Interface ========================
# ===========================================================================
class Reward_Category_ViewSet(ModelViewSet):
    queryset = Reward_Category_model.objects.all()
    serializer_class = Reward_Category_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]  # is_staf = true, is_active = true

    # ---------- Combine All Filters -----------
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "name",
    ]

    pagination_class = user__Pagination  # ---- import (pagination.py) file





# ===========================================================================
# ======================== Reward Category (User) Interface ========================
# ===========================================================================
class Reward_Category_User_ViewSet(ModelViewSet):
    queryset = Reward_Category_model.objects.filter(is_active=True)
    serializer_class = Reward_Category_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]  # is_staf = true, is_active = true

    # ---------- Combine All Filters -----------
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "name",
    ]

    # pagination_class = user__Pagination  # ---- import (pagination.py) file
