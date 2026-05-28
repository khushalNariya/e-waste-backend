from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Reward_Order_Address
from .serializers import Reward_Order_Address_Serializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from app_13_reward_orders.Pagination__File.pagination import user__Pagination
from rest_framework.response import Response

# =========================================================
# ADMIN ORDER ADDRESS API
# =========================================================
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class Admin_Reward_Order_Address_ViewSet(viewsets.ModelViewSet):

    queryset = Reward_Order_Address.objects.all().order_by("-id")
    serializer_class = Reward_Order_Address_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = user__Pagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["full_name", "phone", "city", "order__order_number"]
    filterset_fields = ["order"]


# =========================================================
# USER ORDER ADDRESS API
# =========================================================
class User_Reward_Order_Address_ViewSet(viewsets.ModelViewSet):

    serializer_class = Reward_Order_Address_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reward_Order_Address.objects.filter(
            order__user=self.request.user
        ).order_by("-id")

    def create(self, request, *args, **kwargs):
        user = request.user
        
        # 1. Get unique addresses for the user
        all_user_addresses = Reward_Order_Address.objects.filter(order__user=user)
        unique_addresses = list(all_user_addresses.values('full_name', 'address', 'pincode').distinct())
        
        # 2. Check if the incoming address is new
        incoming_data = request.data
        is_new_unique = True
        for addr in unique_addresses:
            if (addr['full_name'].lower() == str(incoming_data.get('full_name')).lower() and 
                addr['address'].lower() == str(incoming_data.get('address')).lower() and 
                str(addr['pincode']) == str(incoming_data.get('pincode'))):
                is_new_unique = False
                break
        
        # 3. Enforce limit: Max 3 unique addresses
        if is_new_unique and len(unique_addresses) >= 3:
            return Response({
                "error": "Address limit reached (Max 3). Please use or edit an existing address."
            }, status=400)

        # Support for validation only (don't save)
        if request.data.get("validate_only") == True:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                return Response({"message": "Valid"})
            return Response(serializer.errors, status=400)
        
        return super().create(request, *args, **kwargs)
