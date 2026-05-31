from rest_framework.viewsets import ModelViewSet
from app_8_Reward_Rules.models import Reward_Rule_model
from app_8_Reward_Rules.Serializers__Files.reward_rule_serializer import (
    Reward_Rule_Serializer,
)

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.generics import ListAPIView

from app_8_Reward_Rules.DRF__API__app__8__Reward_Rules.pagination import (
    user__Pagination,
)


class Reward_Rule_ViewSet(ModelViewSet):
    queryset = Reward_Rule_model.objects.all().order_by("-id")
    serializer_class = Reward_Rule_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    # 🔍 Search + Order
    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["category__title", "condition__display_name", "points", "unit"]

    ordering_fields = ["id", "points", "created_at"]

    pagination_class = user__Pagination


# ===========================================================================
# ======================== How-It-Works (User/Public) Interface ========================
# ===========================================================================

class Reward_Rule_Public_View(ListAPIView):
    queryset = Reward_Rule_model.objects.filter(is_active=True, condition__is_active=True)
    serializer_class = Reward_Rule_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
