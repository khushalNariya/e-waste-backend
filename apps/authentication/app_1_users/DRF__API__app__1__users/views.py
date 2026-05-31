from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from django.contrib.auth.models import User
from .serializer import RegisterSerializer, UserDetailSerializer,UpdateUserSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
# --- Pagination
from .pagination import user__Pagination  # ---- import (pagination.py) file

from rest_framework_simplejwt.authentication import JWTAuthentication

# ============================== User (side) Register ==============================

class User_RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()

        # Normal user
        user.is_staff = False
        user.is_superuser = False
        user.save()

# ============================== Admin (side) Register ==============================

class Admin_RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()

        # Admin create
        user.is_staff = True
        user.is_superuser = True
        user.save()

# ============================== Admin (side) CURD (Operation) ==============================

class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return RegisterSerializer
    #     return UserDetailSerializer
    def get_serializer_class(self):
        if self.action == "create":
            return RegisterSerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateUserSerializer

        return UserDetailSerializer
    
    # def create(self, request, *args, **kwargs):
    #     serializer = RegisterSerializer(data=request.data)

    #     if serializer.is_valid():
    #         user = serializer.save()

    #         return Response({
    #             "message": "User registered successfully",
    #             "user_id": user.id
    #         }, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 # ---------- Combine All Filters -----------
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        # UserProfile fields
        "profile__mobile_number",
        "profile__city",
        "profile__state",
        "profile__pincode",
    ]
    ordering_fields = ['id',
                       'first_name',
                       'last_name',
                       'email',
                       'profile__city',
                       'profile__state',
                       ]
    # ordering = ['-id']

 # (Type - 1) PageNumberPagination
    pagination_class = user__Pagination  # ---- import (pagination.py) file



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginSerializer

class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ============================== User (side) ==============================

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            data = serializer.validated_data

            if not data["is_active"]:
                return Response(
                    {"error": "Account is inactive"},
                    status=status.HTTP_403_FORBIDDEN
                )

            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ============================== Admin (side) ==============================


# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# @method_decorator(csrf_exempt, name='dispatch')

class AdminLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            data = serializer.validated_data
            print("LOGIN DATA:", data)   # 👈 DEBUG 1

            if not data["is_staff"]:
                print("USER IS NOT STAFF")   # 👈 DEBUG 2

                return Response(
                    {"error": "Admin access only"},
                    status=status.HTTP_403_FORBIDDEN
                )

            if not data["is_active"]:
                print("USER IS NOT ACTIVE")   # 👈 DEBUG 3

                return Response(
                    {"error": "Account is inactive"},
                    status=status.HTTP_403_FORBIDDEN
                )

            return Response(data, status=status.HTTP_200_OK)
        print("SERIALIZER ERROR:", serializer.errors)  # 👈 DEBUG 4

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)