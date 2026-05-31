from django.db import transaction
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from rest_framework.decorators import action

# current module models
from .models import Reward_Order
from .serializers import Reward_Order_Serializer

# other modules in this app
from app_13_reward_orders.Reward_Order_Items__API__2.models import Reward_Order_Item
from app_13_reward_orders.Reward_Order_Address__API__3.models import Reward_Order_Address
from app_13_reward_orders.Reward_Order_Payment__API__4.models import Reward_Order_Payment

# cart tables
from app_12_Reward_Cart.Reward_Cart__API__1.models import Reward_Cart_Model
from app_12_Reward_Cart.Reward_Cart_Items__API__2.models import Reward_Cart_Items_Model

# wallet tables
from app_11_User_Rewards.User_Rewards__API__1.models import (
    User_Wallet_Model,
    Reward_Transaction_Model
)

from app_13_reward_orders.Reward_Order_Status_History__API__5.models import Reward_Order_Status_History


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from app_13_reward_orders.Pagination__File.pagination import user__Pagination


# =========================================================
# ADMIN ORDER API
# Full CRUD
# GET POST PUT PATCH DELETE
# =========================================================
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class Admin_Reward_Order_ViewSet(viewsets.ModelViewSet):

    queryset = Reward_Order.objects.all().order_by("-id")
    serializer_class = Reward_Order_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = user__Pagination
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["order_number", "user__first_name", "user__last_name", "user__email"]
    filterset_fields = ["order_status", "user"]

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        order = serializer.save()

        # =============================================================
        # 🔥 CREATE → FIRST STATUS HISTORY ENTRY (Automatic)
        # =============================================================
        last_history = Reward_Order_Status_History.objects.filter(order=order).order_by("-id").first()
        if not last_history or last_history.status != order.order_status:
            Reward_Order_Status_History.objects.create(
                order=order,
                status=order.order_status,
                changed_by=self.request.user,
                remarks="Order record created by administrator."
            )

    @transaction.atomic
    def perform_update(self, serializer):
        # Get the old status before saving the new one
        old_status = serializer.instance.order_status
        
        # Save the updated order
        order = serializer.save()
        new_status = order.order_status

        # =============================================================
        # 📦 DELIVERED → AUTO SET delivered_at TIMESTAMP
        # =============================================================
        if old_status != "delivered" and new_status == "delivered":
            order.delivered_at = timezone.now()
            order.save(update_fields=["delivered_at"])

        # =============================================================
        # 🔥 REFUND LOGIC → IF ADMIN CANCELS THE ORDER
        # =============================================================
        if old_status != "cancelled" and new_status == "cancelled":
            # 1. Refund points to user's wallet
            wallet, created = User_Wallet_Model.objects.get_or_create(
                user=order.user,
                defaults={"total_points": 0}
            )
            wallet.total_points += order.total_points
            wallet.save()

            # 2. Create a credit transaction record
            Reward_Transaction_Model.objects.create(
                user=order.user,
                points=order.total_points,
                type="credit",
                description=f"Refund for order {order.order_number} (Cancelled by Admin)",
                order=order
            )

        # =============================================================
        # 🔥 UPDATE → STATUS CHANGE HISTORY (Prevent Duplicate)
        # 🔥 UPDATE → STATUS CHANGE HISTORY (With Automated Remarks)
        # =============================================================
        # Get the very last history entry for this order
        last_history = Reward_Order_Status_History.objects.filter(order=order).order_by("-id").first()

        # Only create if the new status is different from the last recorded status
        if not last_history or last_history.status != order.order_status:
            # Generate professional remark based on status
            status_text = order.order_status.replace('_', ' ').title()
            remark_text = f"Status updated to {status_text} by administrator."
            
            if order.order_status == "cancelled":
                remark_text = "Order cancelled by administrator. Points refunded to user's wallet."
            elif order.order_status == "pending":
                remark_text = "Order initiated and awaiting confirmation."

            Reward_Order_Status_History.objects.create(
                order=order,
                status=order.order_status,
                changed_by=self.request.user,
                remarks=remark_text
            )




# =========================================================
# USER ORDER API
# only:
# 1. my orders
# 2. checkout
# =========================================================
class User_Reward_Order_ViewSet(viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reward_Order.objects.all()


    # =====================================================
    # MY ORDERS
    # GET
    # /api/.../User_Reward_Order/
    # =====================================================
    def list(self, request):

        orders = Reward_Order.objects.filter(
            user=request.user
        ).order_by("-id")

        serializer = Reward_Order_Serializer(
            orders,
            many=True
        )

        return Response(serializer.data)


    # =====================================================
    # CHECKOUT
    # POST
    # /api/.../checkout/
    # =====================================================
    @action(detail=False, methods=["post"])
    @transaction.atomic
    def checkout(self, request):
        try:
            user = request.user

            # ==========================================
            # STEP 0: Validate Address
            # ==========================================
            from app_13_reward_orders.Reward_Order_Address__API__3.serializers import Reward_Order_Address_Serializer
            address_serializer = Reward_Order_Address_Serializer(data=request.data)
            if not address_serializer.is_valid():
                return Response(address_serializer.errors, status=400)

            # ==========================================
            # STEP 1: find active cart
            # ==========================================
            cart = Reward_Cart_Model.objects.filter(
                user=user,
                status="active"
            ).first()

            if not cart:
                return Response({"error": "Active cart not found"}, status=400)

            # ==========================================
            # STEP 2: get cart items
            # ==========================================
            cart_items = Reward_Cart_Items_Model.objects.filter(cart=cart)

            if not cart_items.exists():
                return Response({"error": "Your cart is empty"}, status=400)

            total_points = cart.total_points

            # ==========================================
            # STEP 3: check wallet
            # ==========================================
            wallet, created = User_Wallet_Model.objects.get_or_create(
                user=user,
                defaults={"total_points": 0}
            )

            if wallet.total_points < total_points:
                return Response({
                    "error": f"Insufficient points. You have {wallet.total_points} but need {total_points}."
                }, status=400)

            # ==========================================
            # STEP 4: create unique order number
            # ==========================================
            order_number = "ECO-" + timezone.now().strftime("%Y%m%d%H%M%S")

            # ==========================================
            # STEP 5: create order
            # ==========================================
            order = Reward_Order.objects.create(
                order_number=order_number,
                user=user,
                cart_id=cart.id,
                total_points=total_points,
                order_status="pending"
            )

            # =============================================================
            # 🔥 CHECKOUT → INITIAL STATUS HISTORY (Default)
            # =============================================================
            last_history = Reward_Order_Status_History.objects.filter(order=order).order_by("-id").first()
            if not last_history or last_history.status != order.order_status:
                Reward_Order_Status_History.objects.create(
                    order=order,
                    status=order.order_status,
                    changed_by=user,
                    remarks="Order placed successfully via Reward Store."
                )

            # ==========================================
            # STEP 6: copy cart items to order items
            # ==========================================
            for item in cart_items:
                Reward_Order_Item.objects.create(
                    order=order,
                    product_id=item.product.id,
                    product_name=item.product.name,
                    quantity=item.quantity,
                    points=item.points,
                    subtotal_points=item.subtotal_points
                )

            # ==========================================
            # STEP 7: save address
            # ==========================================
            Reward_Order_Address.objects.create(
                order=order,
                full_name=request.data.get("full_name"),
                phone=request.data.get("phone"),
                address=request.data.get("address"),
                city=request.data.get("city"),
                state=request.data.get("state"),
                pincode=request.data.get("pincode"),
                landmark=request.data.get("landmark", "")
            )

            # ==========================================
            # STEP 8: save payment
            # ==========================================
            Reward_Order_Payment.objects.create(
                order=order,
                payment_method=request.data.get("payment_method", "points"),
                payment_status="success",
                amount_points=total_points,
                amount_money=0
            )

            # ==========================================
            # STEP 9: deduct wallet points
            # ==========================================
            wallet.total_points -= total_points
            wallet.save()

            # ==========================================
            # STEP 10: save debit transaction
            # ==========================================
            Reward_Transaction_Model.objects.create(
                user=user,
                points=total_points,
                type="debit",
                description=f"Reward order {order_number}",
                submission=None,
                order=order  # Linked to the newly created order
            )


            # ==========================================
            # STEP 11: close cart
            # ==========================================
            cart.status = "checked_out"
            cart.save()

            return Response({
                "message": "Order created successfully",
                "order_number": order_number
            })

        except Exception as e:
            return Response({"error": str(e)}, status=500)


    # =====================================================



    # =====================================================
    # CANCEL ORDER
    # POST
    # /api/.../cancel_order/
    # =====================================================
    @action(detail=False, methods=["post"])
    @transaction.atomic
    def cancel_order(self, request):
        
        order_number = request.data.get("order_number")
        reason = request.data.get("reason", "No reason provided")

        order = Reward_Order.objects.filter(
            order_number=order_number,
            user=request.user
        ).first()

        if not order:
            return Response({"error": "Order not found"}, status=404)

        if order.order_status not in ["pending", "confirmed", "processing", "packed"]:
            return Response({
                "error": "This order has already been processed for shipping and cannot be cancelled through the portal. Please contact our Support Team or visit the Contact Us page for assistance."
            }, status=400)

        # Update order status
        order.order_status = "cancelled"
        order.save()

        # =============================================================
        # 🔥 CANCEL → LOG STATUS HISTORY (Prevent Duplicate)
        # =============================================================
        last_history = Reward_Order_Status_History.objects.filter(order=order).order_by("-id").first()
        if not last_history or last_history.status != order.order_status:
            Reward_Order_Status_History.objects.create(
                order=order,
                status=order.order_status,
                changed_by=request.user,
                remarks=f"Cancelled by user. Reason: {reason}"
            )

        # Refund points
        wallet = User_Wallet_Model.objects.get(user=request.user)
        wallet.total_points += order.total_points
        wallet.save()

        # Save credit transaction
        Reward_Transaction_Model.objects.create(
            user=request.user,
            points=order.total_points,
            type="credit",
            description=f"Refund for cancelled order {order_number}"
        )

        return Response({
            "message": "Order cancelled successfully",
            "order_number": order_number
        })

