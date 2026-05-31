from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from app_15_reward_replaces.Reward_Order_Replace_Status_History__API__3.models import Reward_Order_Replace_Status_History
from app_15_reward_replaces.Reward_Order_Replace_Status_History__API__3.serializers import Reward_Order_Replace_Status_History_Serializer
from app_15_reward_replaces.Pagination__File.pagination import RewardReplace_Pagination


# =============================================================
# ADMIN STATUS HISTORY VIEWSET
# Admin can list all history logs and update remarks only.
# Status column is protected — cannot be changed here.
# =============================================================
class Admin_Reward_Order_Replace_Status_History_ViewSet(viewsets.ModelViewSet):
    queryset           = Reward_Order_Replace_Status_History.objects.all().order_by("-id")
    serializer_class   = Reward_Order_Replace_Status_History_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class   = RewardReplace_Pagination

    # Override update to block 'status' field changes via this endpoint.
    # Status changes must go through the main replace request update endpoint.
    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        # Remove status from payload — it is system-controlled only
        data.pop("status", None)

        serializer = self.get_serializer(self.get_object(), data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


# =============================================================
# USER STATUS HISTORY VIEWSET (Read Only)
# Users can only see history logs for their own replace requests.
# =============================================================
class User_Reward_Order_Replace_Status_History_ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class   = Reward_Order_Replace_Status_History_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class   = RewardReplace_Pagination

    # Filter to only return history for the current user's replace requests
    def get_queryset(self):
        return Reward_Order_Replace_Status_History.objects.filter(
            replace_request__user=self.request.user
        ).order_by("-id")
