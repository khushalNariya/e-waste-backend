from django.db import transaction
from rest_framework import viewsets, filters, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

# Model and serializer imports
from app_14_reward_returns.Reward_Order_Return_Request__API__1.models import Reward_Order_Return_Request
from app_14_reward_returns.Reward_Order_Return_Request__API__1.serializers import Reward_Order_Return_Request_Serializer
from app_14_reward_returns.Reward_Order_Return_Status_History__API__3.models import Reward_Order_Return_Status_History
from app_14_reward_returns.Reward_Order_Return_Pickups__API__4.models import Reward_Order_Return_Pickup

# Other app dependencies
from app_11_User_Rewards.User_Rewards__API__1.models import User_Wallet_Model, Reward_Transaction_Model
from app_14_reward_returns.Pagination__File.pagination import RewardReturn_Pagination

# =========================================================
# 👑 ADMIN RETURN REQUESTS VIEWSET (MODELVIEWSET)
# =========================================================
class Admin_Reward_Order_Return_Request_ViewSet(viewsets.ModelViewSet):
    queryset = Reward_Order_Return_Request.objects.all().order_by("-id")
    serializer_class = Reward_Order_Return_Request_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = RewardReturn_Pagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["return_number", "order__order_number", "user__first_name", "user__last_name", "user__email"]
    filterset_fields = ["return_status", "user"]
    ordering_fields = ["created_at", "id"]

    # Support partial updates by default
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    # =========================================================
    # 🔥 AUTOMATED STATUS TRANSITIONS & REFUND LOGIC
    # =========================================================
    @transaction.atomic
    def perform_update(self, serializer):
        # Get status states before committing save
        old_instance = self.get_object()
        old_status = old_instance.return_status
        return_request = serializer.save()
        new_status = return_request.return_status

        # Execute only if there is a real status transition
        if old_status != new_status:
            
            # Step 1: Generate dynamic system remarks based on status change
            status_display = new_status.replace('_', ' ').title()
            remark_text = f"Return request status updated to {status_display} by administrator."

            # Step 2: Handle Automated Pickup updates & specific remarks
            pickup = Reward_Order_Return_Pickup.objects.filter(return_request=return_request).first()

            if new_status == "approved":
                remark_text = "Return request approved by administrator. Pickup agent will schedule courier shortly."
                if pickup:
                    pickup.pickup_status = "scheduled"
                    pickup.save()

            elif new_status == "pickup_scheduled":
                remark_text = "Pickup scheduled successfully. Date of courier visit set."

            elif new_status == "picked_up":
                remark_text = "Courier picked up the product successfully. Transit to warehouse initiated."
                if pickup:
                    pickup.pickup_status = "picked_up"
                    pickup.save()

            elif new_status == "received":
                remark_text = "Returned item received safely at processing warehouse."

            elif new_status == "inspected":
                remark_text = "Inspection completed by quality check agent. Product condition verified."

            elif new_status == "refund_approved":
                remark_text = "Refund approved by administrator. Wallet points settlement queued."

            # =========================================================
            # 🔥 AUTOMATED REFUND TRIGGER (ON REFUNDED)
            # =========================================================
            elif new_status == "refunded":
                remark_text = f"Points successfully refunded to wallet. Settled points value: {return_request.refund_points} pts."
                
                # Deduct points from user's wallet
                wallet, created = User_Wallet_Model.objects.get_or_create(
                    user=return_request.user,
                    defaults={"total_points": 0}
                )
                wallet.total_points += return_request.refund_points
                wallet.save()

                # Save credit transaction audit log
                Reward_Transaction_Model.objects.create(
                    user=return_request.user,
                    points=return_request.refund_points,
                    type="credit",
                    description=f"Points Refunded for Return Request {return_request.return_number}",
                    order=return_request.order
                )

            elif new_status == "rejected":
                remark_text = "Return request rejected by administrator due to inspection failure or policy violation."
                if pickup:
                    pickup.pickup_status = "failed"
                    pickup.save()

            # Step 3: Write to audit status history table
            Reward_Order_Return_Status_History.objects.create(
                return_request=return_request,
                status=new_status,
                changed_by=self.request.user,
                remarks=remark_text
            )


# =========================================================
# 👤 USER RETURN REQUESTS VIEWSET (GENERICVIEWSET)
# =========================================================
class User_Reward_Order_Return_Request_ViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = Reward_Order_Return_Request_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = RewardReturn_Pagination

    # Restrict users to only see their own return requests
    def get_queryset(self):
        return Reward_Order_Return_Request.objects.filter(
            user=self.request.user
        ).order_by("-id")

    # Custom cancel action for return request (sets status to 'rejected' as exit state)
    from rest_framework.decorators import action
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    @transaction.atomic
    def cancel(self, request, pk=None):
        return_request = self.get_object()
        
        # Can only cancel if status is still 'requested'
        if return_request.return_status != 'requested':
            return Response(
                {"error": f"Cannot cancel return request. Current status is '{return_request.return_status}'."},
                status=400
            )
            
        # Read user-provided cancellation reason from POST body
        cancel_reason = request.data.get('reason', '').strip()
        base_remark = "Return request cancelled by customer."
        remarks = f"{base_remark} Reason: {cancel_reason}" if cancel_reason else base_remark

        return_request.return_status = 'rejected'
        return_request.save()
        
        # Write to audit status history
        Reward_Order_Return_Status_History.objects.create(
            return_request=return_request,
            status='rejected',
            changed_by=request.user,
            remarks=remarks
        )
        
        return Response({"message": "Return request cancelled successfully.", "status": "rejected"})
