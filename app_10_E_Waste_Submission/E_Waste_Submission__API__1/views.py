from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from app_10_E_Waste_Submission.E_Waste_Submission__API__1.models import (
    E_Waste_Submission_Model,
)
from app_10_E_Waste_Submission.E_Waste_Submission__API__1.serializers import (
    E_Waste_Submission_Serializer,
)

# Import from separate pagination folder
from app_10_E_Waste_Submission.Pagination__File.pagination import (
    EWasteSubmission_Pagination,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from app_10_E_Waste_Submission.E_Waste_Submission_Images__API__2.models import (
    E_Waste_Submission_Images_Model,
)
from rest_framework.response import Response

from app_10_E_Waste_Submission.E_Waste_Status_History__API__3.models import (
    E_Waste_Status_History_Model,
)
from app_10_E_Waste_Submission.E_Waste_Submission__API__1.reward_logic import (
    process_reward,
)
from app_8_Reward_Rules.models import Reward_Rule_model
from app_11_User_Rewards.User_Rewards__API__1.models import (
    Reward_Transaction_Model,
    User_Wallet_Model,
)
from rest_framework import mixins


class E_Waste_Submission_ViewSet(viewsets.ModelViewSet):
    queryset = E_Waste_Submission_Model.objects.all().order_by("created_at")
    serializer_class = E_Waste_Submission_Serializer
    pagination_class = EWasteSubmission_Pagination

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [
        IsAdminUser
    ]  # Changed from IsAdminUser to allow regular users to submit

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ["user", "status", "pickup_type", "category"]
    search_fields = ["user__first_name", "user__last_name", "phone", "notes"]
    ordering_fields = ["created_at", "pickup_date", "id"]

    # =========================
    # For partial update
    # =========================
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    # ===============================
    # 🔥 CREATE → FIRST HISTORY ENTRY
    # ===============================
    def perform_create(self, serializer):
        submission = serializer.save()

        # from app_10_E_Waste_Submission.E_Waste_Status_History__API__3.models import (
        #     E_Waste_Status_History_Model
        # )

        E_Waste_Status_History_Model.objects.create(
            submission=submission,
            status=submission.status,  # default = requested
            changed_by=self.request.user,
        )

    # ===============================
    # 🔥 UPDATE → STATUS CHANGE HISTORY
    # ===============================
    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_status = old_instance.status

        submission = serializer.save()

        # from app_10_E_Waste_Submission.E_Waste_Status_History__API__3.models import (
        #     E_Waste_Status_History_Model
        # )

        # 🔥 Only if status changed
        # ===============================
        # 🔹 STATUS HISTORY (already hai)
        # ===============================

        # duplicate entry nahi banegi
        if old_status != submission.status:
            E_Waste_Status_History_Model.objects.create(
                submission=submission,
                status=submission.status,
                changed_by=self.request.user,
                # ❌ remarks remove kar diya
            )

        # =========================================================
        # 🔥 REWARD LOGIC (FINAL CORRECT VERSION)
        # =========================================================

        # ✅ STEP 1: Only when status becomes rewarded

        # Reward logic duplicate fire na ho
        reward_should_run = False

        # ✅ Case 1: First time rewarded
        if submission.status == "rewarded" and old_status != "rewarded":
            reward_should_run = True

        # ✅ Case 2: Already rewarded but data changed
        elif submission.status == "rewarded" and old_status == "rewarded":
            if (
                old_instance.final_condition != submission.final_condition
                or old_instance.weight != submission.weight
            ):
                reward_should_run = True

        # ===============================
        # 🔥 CALL REWARD FUNCTION
        # ===============================
        if reward_should_run:
            process_reward(submission, old_instance)


# ==============================================================
# ===================== User (Api) View-set ====================
# ==============================================================


class User_EWaste_Submission_ViewSet(
    mixins.CreateModelMixin,  # create (post)
    mixins.ListModelMixin,  # read (get)
    viewsets.GenericViewSet,  # viewset
):
    serializer_class = E_Waste_Submission_Serializer
    # 👉 Only logged-in users can access this API
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # ------------- Get (login) User Data
    def get_queryset(self):
        return E_Waste_Submission_Model.objects.filter(
            user=self.request.user  # 👉 Show only current user's data
        )

    # ------------- POST (CREATE)
    def perform_create(self, serializer):
        submission = serializer.save(
            user=self.request.user,  # 👉 Automatically set logged-in user
            # status="requested"
        )

        # status History (Create) Automatic
        E_Waste_Status_History_Model.objects.create(
            submission=submission,  # 👉 Link with submission
            status=submission.status,  # 👉 Current status
            changed_by=self.request.user,  # 👉 Who made this change
        )
