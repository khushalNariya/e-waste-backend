# views.py

from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from .models import Reward_Product_model
from .serializers import Reward_Product_Serializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

# pagi
from ..Pagination__File.pagination import user__Pagination


# ===========================================================================
# ======================== Reward Product (Admin) Interface ========================
# ===========================================================================
class Reward_Product_ViewSet(ModelViewSet):

    queryset = Reward_Product_model.objects.all().order_by("-id")
    serializer_class = Reward_Product_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["category"]

    search_fields = [
        "name",
    ]

    ordering_fields = ["id", "points", "created_at"]

    pagination_class = user__Pagination

    # Partial update support
    def update(self, request, *args, **kwargs):

        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# ===========================================================================
# ======================== Reward Product (User) Interface ========================
# ===========================================================================
class Reward_Product_User_ViewSet(ModelViewSet):

    queryset = Reward_Product_model.objects.filter(is_active=True, category__is_active=True).order_by("-id")
    serializer_class = Reward_Product_Serializer
    lookup_field = "slug"

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["category"]

    search_fields = [
        "name",
    ]

    # ordering_fields = ["id"]

    # pagination_class = user__Pagination
