from rest_framework.viewsets import ModelViewSet
from app_5_Home.models import HowItWorks_model,Hero_Section_model
from .serializer import HowItWorks_Serializer,Hero_Section_Serializer
from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.authentication import SessionAuthentication

# --- Pagination
from .pagination import user__Pagination  # ---- import (pagination.py) file
from rest_framework.permissions import IsAdminUser,IsAuthenticated

# ===========================================================================
# ======================== How-It-Works (Admin) Interface ========================
# ===========================================================================

class HowItWorks_ViewSet(ModelViewSet):
    queryset = HowItWorks_model.objects.all()
    serializer_class = HowItWorks_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser] # is_staf = true, is_active = true

# ---------- Combine All Filters -----------
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "title",
    ]

    pagination_class = user__Pagination  # ---- import (pagination.py) file




# ===========================================================================
# ======================== How-It-Works (User/Public) Interface ========================
# ===========================================================================
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class HowItWorks_Public_View(ListAPIView):
    queryset = HowItWorks_model.objects.filter(is_active=True)
    serializer_class = HowItWorks_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



# ===========================================================================
# ======================== Hero-Section (Admin) Interface ========================
# ===========================================================================

class Hero_Section_Admin_ViewSet(ModelViewSet):
    queryset = Hero_Section_model.objects.all()
    serializer_class = Hero_Section_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser] # is_staf = true, is_active = true
    pagination_class = user__Pagination  # ---- import (pagination.py) file

    def update(self, request, *args, **kwargs):
                partial = kwargs.pop('partial', True)
                instance = self.get_object()
                serializer = self.get_serializer(
                        instance,
                        data=request.data,
                        partial=partial
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)


class Hero_Section_Public_View(ListAPIView):
    queryset = Hero_Section_model.objects.filter(is_active=True)
    serializer_class = Hero_Section_Serializer
    permission_classes = [AllowAny]
