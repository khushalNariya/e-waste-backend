from django.db import transaction
from rest_framework import viewsets, filters, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.models import (
    Reward_Order_Replace_Request,
)
from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.serializers import (
    Reward_Order_Replace_Request_Serializer,
)
from app_15_reward_replaces.Reward_Order_Replace_Status_History__API__3.models import (
    Reward_Order_Replace_Status_History,
)
from app_15_reward_replaces.Reward_Order_Replace_Pickups__API__4.models import (
    Reward_Order_Replace_Pickup,
)
from app_15_reward_replaces.Pagination__File.pagination import RewardReplace_Pagination


# =============================================================
# ADMIN REPLACE REQUESTS VIEWSET
# Full CRUD — Admin can view all requests and update status
# =============================================================
class Admin_Reward_Order_Replace_Request_ViewSet(viewsets.ModelViewSet):
    queryset = Reward_Order_Replace_Request.objects.all().order_by("-id")
    serializer_class = Reward_Order_Replace_Request_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = RewardReplace_Pagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        "replace_number",
        "order__order_number",
        "user__first_name",
        "user__last_name",
        "user__email",
    ]
    filterset_fields = ["replace_status", "user"]
    ordering_fields = ["created_at", "id"]

    # Allow partial updates (PATCH-like behavior on PUT too)
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    # =========================================================
    # AUTOMATED STATUS TRANSITIONS ON ADMIN UPDATE
    # Each status change triggers specific actions automatically
    # =========================================================
    @transaction.atomic
    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_status = old_instance.replace_status
        replace_request = serializer.save()
        new_status = replace_request.replace_status

        # Only act if status actually changed
        if old_status != new_status:

            # Default remark text (overridden per status below)
            status_display = new_status.replace("_", " ").title()
            remark_text = (
                f"Replace request status updated to {status_display} by administrator."
            )

            # Get pickup record linked to this replace request
            pickup = Reward_Order_Replace_Pickup.objects.filter(
                replace_request=replace_request
            ).first()

            if new_status == "approved":
                # Admin verified the claim — replacement will be prepared
                remark_text = "Replace request approved. Replacement item will be dispatched shortly."

            elif new_status == "replacement_dispatched":
                # New item sent to courier — courier will deliver new + collect old in one trip
                remark_text = "Replacement item dispatched via courier. Agent will deliver new item and collect old item at the same time."
                if pickup:
                    pickup.pickup_status = "scheduled"
                    pickup.save()

            elif new_status == "replacement_delivered":
                # Delivery done — new item handed to user, old item collected
                remark_text = "Replacement delivered to customer. Old item collected by courier agent."
                if pickup:
                    pickup.pickup_status = "picked_up"
                    pickup.save()



            elif new_status == "rejected":
                # Claim was invalid or item was tampered
                remark_text = "Replace request rejected by administrator. Claim could not be verified."
                if pickup:
                    pickup.pickup_status = "failed"
                    pickup.save()

            # Write status change to audit history table
            Reward_Order_Replace_Status_History.objects.create(
                replace_request=replace_request,
                status=new_status,
                changed_by=self.request.user,
                remarks=remark_text,
            )


# =============================================================
# USER REPLACE REQUESTS VIEWSET
# User can: create a request, list own requests, view detail
# User cannot: update or delete
# =============================================================
class User_Reward_Order_Replace_Request_ViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = Reward_Order_Replace_Request_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = RewardReplace_Pagination

    # Users only see their own replace requests
    def get_queryset(self):
        return Reward_Order_Replace_Request.objects.filter(
            user=self.request.user
        ).order_by("-id")

    # Custom cancel action for replacement request (sets status to 'rejected' as exit state)
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    @transaction.atomic
    def cancel(self, request, pk=None):
        replace_request = self.get_object()

        # Can only cancel if status is still 'requested'
        if replace_request.replace_status != "requested":
            return Response(
                {
                    "error": f"Cannot cancel replace request. Current status is '{replace_request.replace_status}'."
                },
                status=400,
            )

        # Read user-provided cancellation reason from POST body
        cancel_reason = request.data.get('reason', '').strip()
        base_remark = "Replace request cancelled by customer."
        remarks = f"{base_remark} Reason: {cancel_reason}" if cancel_reason else base_remark

        replace_request.replace_status = "rejected"
        replace_request.save()

        # Write to audit status history
        Reward_Order_Replace_Status_History.objects.create(
            replace_request=replace_request,
            status="rejected",
            changed_by=request.user,
            remarks=remarks,
        )

        return Response(
            {"message": "Replace request cancelled successfully.", "status": "rejected"}
        )
