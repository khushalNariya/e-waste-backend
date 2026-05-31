from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from django.db import transaction

from .models import (
    Reward_Cart_Model,
    Reward_Cart_Items_Model
)

from .serializers import (
    Reward_Cart_Items_Serializer
)

from django.db import models
from app_9_Reward_Products.Reward_Product__API__2.models import Reward_Product_model
from rest_framework.permissions import IsAdminUser,AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from app_12_Reward_Cart.Pagination__File.pagination import user__Pagination
from django.shortcuts import get_object_or_404


# ============================================================
# ADMIN CART ITEMS VIEWSET
# ============================================================

class Admin_Reward_Cart_Items_ViewSet(viewsets.ModelViewSet):

    queryset = Reward_Cart_Items_Model.objects.all().order_by("-id")

    serializer_class = Reward_Cart_Items_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = user__Pagination

    # Filter - Reward-Cart-Items (Admin - User interface)
    def get_queryset(self):
        queryset = Reward_Cart_Items_Model.objects.all().order_by("-id")
        cart_id = self.request.query_params.get("cart")
        user_id = self.request.query_params.get("user")
        category_id = self.request.query_params.get("category")
        product_id = self.request.query_params.get("product")

        if cart_id:
            queryset = queryset.filter(cart_id=cart_id)
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        if user_id:
            queryset = queryset.filter(cart__user_id=user_id)
        if category_id:
            queryset = queryset.filter(product__category_id=category_id)

        return queryset


# ============================================================
# USER CART ITEMS VIEWSET
# ============================================================

class User_Reward_Cart_Items_ViewSet(viewsets.ModelViewSet):

    serializer_class = Reward_Cart_Items_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # Only Login User Items
    def get_queryset(self):

        return Reward_Cart_Items_Model.objects.filter(
            cart__user=self.request.user,
            cart__status="active"
        ).order_by("-id")

    # ADD TO CART
    @transaction.atomic
    def create(self, request, *args, **kwargs):

        product_id = request.data.get("product")

        quantity = int(request.data.get("quantity", 1))
        
        if quantity < 1:
            return Response({"error": "Quantity must be at least 1"}, status=400)

        # Product
        # product = Reward_Product_model.objects.get(id=product_id)
        product = get_object_or_404(
            Reward_Product_model,
            id=product_id
        )
        
        # Active Cart
        cart = Reward_Cart_Model.objects.filter(
            user=request.user,
            status="active"
        ).first()

        if not cart:
            cart = Reward_Cart_Model.objects.create(
                user=request.user,
                status="active"
            )

        # Product Points
        points = product.points

        subtotal = points * quantity

        # Already Exists
        item = Reward_Cart_Items_Model.objects.filter(
            cart=cart,
            product=product
        ).first()

        # Update Existing
        if item:

            item.quantity += quantity

            item.subtotal_points = item.quantity * item.points

            item.save()

        else:

            Reward_Cart_Items_Model.objects.create(
                cart=cart,
                product=product,
                quantity=quantity,
                points=points,
                subtotal_points=subtotal
            )

        # Update Cart Total
        total = Reward_Cart_Items_Model.objects.filter(
            cart=cart
        ).aggregate(total=models.Sum("subtotal_points"))["total"] or 0

        cart.total_points = total

        cart.save()

        return Response({
            "message": "Product added to cart successfully"
        })

    # UPDATE QUANTITY
    @transaction.atomic
    def partial_update(self, request, *args, **kwargs):

        item = self.get_object()

        quantity = int(request.data.get("quantity"))
        
        if quantity < 1:
            return Response({"error": "Quantity must be at least 1"}, status=400)

        item.quantity = quantity

        item.subtotal_points = quantity * item.points

        item.save()

        # Update Cart Total
        cart = item.cart

        total = Reward_Cart_Items_Model.objects.filter(
            cart=cart
        ).aggregate(total=models.Sum("subtotal_points"))["total"] or 0

        cart.total_points = total

        cart.save()

        serializer = self.get_serializer(item)

        return Response(serializer.data)

    # DELETE ITEM
    @transaction.atomic
    def destroy(self, request, *args, **kwargs):

        item = self.get_object()

        cart = item.cart

        item.delete()

        # Update Cart Total
        total = Reward_Cart_Items_Model.objects.filter(
            cart=cart
        ).aggregate(total=models.Sum("subtotal_points"))["total"] or 0

        cart.total_points = total

        cart.save()

        return Response({
            "message": "Item removed from cart"
        })