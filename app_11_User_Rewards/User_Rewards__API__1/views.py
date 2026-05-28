from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User_Wallet_Model, Reward_Transaction_Model
from .serializers import User_Wallet_Serializer, Reward_Transaction_Serializer

from app_11_User_Rewards.Pagination__File.pagination import user__Pagination

# ===============================
# 🔹 USER WALLET VIEWSET
# ===============================
class User_Wallet_ViewSet(viewsets.ModelViewSet):
    queryset = User_Wallet_Model.objects.all()
    serializer_class = User_Wallet_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = user__Pagination

    # 👇 User apna wallet hi dekhe
    # def get_queryset(self):
    #     return User_Wallet_Model.objects.filter(user=self.request.user)


# ===============================
# 🔹 REWARD TRANSACTION VIEWSET
# ===============================
class Reward_Transaction_ViewSet(viewsets.ModelViewSet):
    queryset = Reward_Transaction_Model.objects.all().order_by("-created_at")
    serializer_class = Reward_Transaction_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = user__Pagination
    
    # 👇 User apne hi transactions dekhe
    # def get_queryset(self):
    #     return Reward_Transaction_Model.objects.filter(user=self.request.user)



# ============================================================================
# ============================================================================
# ============================================================================
# views_user.py

class User_Wallet_User_ViewSet(viewsets.ModelViewSet):
    queryset = User_Wallet_Model.objects.all()
    serializer_class = User_Wallet_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 👤 Sirf apna wallet
        return User_Wallet_Model.objects.filter(user=self.request.user)

# ============================================================================
class Reward_Transaction_User_ViewSet(viewsets.ModelViewSet):
    queryset = Reward_Transaction_Model.objects.all()
    serializer_class = Reward_Transaction_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 👤 Sirf apni history
        return Reward_Transaction_Model.objects.filter(user=self.request.user)