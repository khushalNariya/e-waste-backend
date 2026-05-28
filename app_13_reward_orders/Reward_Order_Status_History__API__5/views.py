from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Reward_Order_Status_History
from .serializers import Reward_Order_Status_History_Serializer

from app_13_reward_orders.Pagination__File.pagination import (
    user__Pagination,
)

# Admin ViewSet
class Reward_Order_Status_History_ViewSet(viewsets.ModelViewSet):
    queryset = (
        Reward_Order_Status_History.objects.select_related(
            "order",
            "order__user",
            "changed_by",
        ).order_by("-created_at")
    )
    serializer_class = Reward_Order_Status_History_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["order", "status", "order__user"]
    search_fields = [
        "order__order_number",
        "order__user__username",
        "changed_by__username",
    ]
    ordering_fields = ["created_at", "id"]
    pagination_class = user__Pagination

    # ============================================================================
    # 🔥 CUSTOM UPDATE: Only allow updating 'remarks', prevent changing 'status'
    # ============================================================================
    def update(self, request, *args, **kwargs):
        data = request.data.copy()  # Make data mutable (so we can pop fields)

        # ⛔ Remove 'status' and 'order' because they should never change in history
        data.pop("status", None)
        data.pop("order", None)
        data.pop("changed_by", None)

        # 📝 Perform partial update to update only allowed fields (like remarks)
        serializer = self.get_serializer(self.get_object(), data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

# User ViewSet
class User_Reward_Order_Status_History_ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = Reward_Order_Status_History_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reward_Order_Status_History.objects.filter(
            order__user=self.request.user
        ).order_by("created_at")
