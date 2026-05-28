from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from django.db import transaction

from .models import (
    Reward_Cart_Model,
)

from .serializers import (
    Reward_Cart_Serializer
)

from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from app_12_Reward_Cart.Pagination__File.pagination import user__Pagination

# ============================================================
# ADMIN CART API
# ============================================================

class Admin_Reward_Cart_ViewSet(viewsets.ModelViewSet):

    queryset = Reward_Cart_Model.objects.all().order_by("-id")

    serializer_class = Reward_Cart_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = user__Pagination

    # Filter - Reward-Cart (Admin - User interface)
    def get_queryset(self):
        queryset = Reward_Cart_Model.objects.all().order_by("-id")
        user_id = self.request.query_params.get("user")
        status = self.request.query_params.get("status")

        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if status:
            queryset = queryset.filter(status=status)

        return queryset

# ============================================================
# USER CART API
# ============================================================

class User_Reward_Cart_ViewSet(viewsets.ModelViewSet):

    serializer_class = Reward_Cart_Serializer
    # jwt_authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # Only Login User Cart
    def get_queryset(self):

        return Reward_Cart_Model.objects.filter(
            user=self.request.user
        ).order_by("-id")

    # Auto Create Cart
    def list(self, request, *args, **kwargs):

        cart = Reward_Cart_Model.objects.filter(
            user=request.user,
            status="active"
        ).first()

        if not cart:
            cart = Reward_Cart_Model.objects.create(
                user=request.user,
                status="active"
            )

        serializer = self.get_serializer(cart)

        return Response(serializer.data)