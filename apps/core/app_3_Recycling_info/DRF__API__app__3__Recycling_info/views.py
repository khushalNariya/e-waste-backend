from app_3_Recycling_info.models import Recycle_Category
from .serializer import Recycle_Serializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# --- Pagination
from .pagination import user__Pagination  # ---- import (pagination.py) file


class Recycle_Admin_View(ModelViewSet):

    queryset = Recycle_Category.objects.all()
    serializer_class = Recycle_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser] # is_staf = true, is_active = true

# ---------- Combine All Filters -----------
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "title",
    ]

    pagination_class = user__Pagination  # ---- import (pagination.py) file

# ===========================================================================
# ======================== All-Recycle-Category-Fatch (Admin) Interface ========================
# ===========================================================================
class All_Recycle_Category_Fatch_View(ListAPIView):

    queryset = Recycle_Category.objects.all()
    serializer_class = Recycle_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser] # is_staf = true, is_active = true


# ===========================================================================
# ======================== Recycle (Public) Interface ========================
# ===========================================================================
class Recycle_ListAPIView(ListAPIView):

    queryset = Recycle_Category.objects.all()
    serializer_class = Recycle_Serializer

