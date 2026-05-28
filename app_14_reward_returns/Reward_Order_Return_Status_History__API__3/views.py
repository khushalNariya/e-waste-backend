from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from app_14_reward_returns.Reward_Order_Return_Status_History__API__3.models import Reward_Order_Return_Status_History
from app_14_reward_returns.Reward_Order_Return_Status_History__API__3.serializers import Reward_Order_Return_Status_History_Serializer
from app_14_reward_returns.Pagination__File.pagination import RewardReturn_Pagination

# ============================================================================
# Admin-side ViewSet for Return Status History
# ============================================================================
class Admin_Reward_Order_Return_Status_History_ViewSet(viewsets.ModelViewSet):
    queryset = Reward_Order_Return_Status_History.objects.all().order_by("-id")
    serializer_class = Reward_Order_Return_Status_History_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = RewardReturn_Pagination

    # 🔥 Custom Update Method: Prevents changing 'status' via PUT/PATCH, only allows updating remarks
    def update(self, request, *args, **kwargs):
        data = request.data.copy()  # Make data mutable (so we can pop fields)

        # Remove 'status' if present, because status changes should only happen via NEW history entries (create)
        data.pop("status", None)

        # Perform partial update (PATCH like behavior) to update only remarks or other allowed fields
        serializer = self.get_serializer(self.get_object(), data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

# ============================================================================
# User-side ViewSet for Return Status History
# ============================================================================
class User_Reward_Order_Return_Status_History_ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = Reward_Order_Return_Status_History_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = RewardReturn_Pagination

    def get_queryset(self):
        # Only show history logs belonging to the currently logged in user
        return Reward_Order_Return_Status_History.objects.filter(
            return_request__user=self.request.user
        ).order_by("-id")
