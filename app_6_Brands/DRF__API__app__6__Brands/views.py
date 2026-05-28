from rest_framework.viewsets import ModelViewSet
from app_6_Brands.models import Brand
from .serializer import Brand_Serializer
from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView

# --- Pagination
from .pagination import user__Pagination  # ---- import (pagination.py) file
from rest_framework.permissions import IsAdminUser,IsAuthenticated

# ===========================================================================
# ======================== Brands (Admin) Interface ========================
# ===========================================================================
class Brand_ViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = Brand_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser] # is_staf = true, is_active = true

# ---------- Combine All Filters -----------
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "name",
    ]

    pagination_class = user__Pagination  # ---- import (pagination.py) file


# ===========================================================================
# ======================== Brands (User) Interface ========================
# ===========================================================================
class All_Brand_Fatch_ViewSet(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = Brand_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser] # is_staf = true, is_active = true
