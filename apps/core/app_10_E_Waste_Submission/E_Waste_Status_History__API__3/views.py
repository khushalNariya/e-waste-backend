from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import E_Waste_Status_History_Model
from .serializers import E_Waste_Status_History_Serializer

from app_10_E_Waste_Submission.Pagination__File.pagination import (
    EWasteSubmission_Pagination,
)


# API ViewSet to handle E-Waste Status History records
class E_Waste_Status_History_ViewSet(viewsets.ModelViewSet):

    # Optimized Queryset: join tables (select_related) and pre-fetch images (prefetch_related) to avoid N+1 issues
    queryset = (
        E_Waste_Status_History_Model.objects.select_related(
            "submission__user",
            "submission__model__category",
            "submission__model__brand",
            "changed_by",
        )
        .prefetch_related("submission__images")
        .order_by("-created_at")
    )

    serializer_class = E_Waste_Status_History_Serializer

    # Auth: JWT for mobile/modern apps, Session for browser testing
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    # Restrict to Admin/Staff only
    permission_classes = [IsAdminUser]

    # Backend filtering (exact match), Search (text based), and Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # ADDED: (Front side) Filteration
    filterset_fields = ["submission", "status", "submission__user", "submission__category"]
    search_fields = [
        "submission__id",
        "submission__user__first_name",
        "submission__user__last_name",
        "submission__model__model_name",
        "submission__model__category__title",
        "submission__model__brand__name",
        "changed_by__first_name",
        "changed_by__last_name",
    ]
    ordering_fields = ["created_at", "id"]
    pagination_class = EWasteSubmission_Pagination

    # 🔥 Custom Update Method: Prevents changing 'status' via PUT/PATCH, only allows updating remarks
    def update(self, request, *args, **kwargs):
        data = request.data.copy()  # Make data mutable (so we can pop fields)

        # Remove 'status' if present, because status changes should only happen via NEW history entries (create)
        data.pop("status", None)

        # Perform partial update (PATCH like behavior) to update only remarks or other allowed fields
        serializer = self.get_serializer(self.get_object(), data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)






# ============================================================================
# User-side ViewSet for E-Waste Status History
class User_EWaste_Status_History_ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = E_Waste_Status_History_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show history for submissions belonging to the current user
        return E_Waste_Status_History_Model.objects.filter(
            submission__user=self.request.user
        ).order_by("created_at")

