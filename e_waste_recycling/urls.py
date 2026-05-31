from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app_1_users.DRF__API__app__1__users.views import (
    RegisterViewSet,
    LoginView,
    UserLoginView,
    AdminLoginView,
    User_RegisterViewSet,
    Admin_RegisterViewSet,
)
from app_3_Recycling_info.DRF__API__app__3__Recycling_info.views import (
    Recycle_Admin_View,
    Recycle_ListAPIView,
)
from app_4_Education.DRF__API__app__4__Education.views import Education_view_set
from app_5_Home.DRF__API__app__5__Home.views import (
    HowItWorks_ViewSet,
    Hero_Section_Admin_ViewSet,
)
from app_6_Brands.DRF__API__app__6__Brands.views import Brand_ViewSet
from app_7_Category_Brand_Mapping.DRF__API__app__7__Category_Brand_Mapping.views import (
    Category_Brand_Mapping_ViewSet,
)
from app_7_Category_Brand_Mapping.Product__Model__Name____API.product__Model___View import (
    Product_Model_Name_ViewSet,
)

from app_8_Reward_Rules.DRF__API__app__8__Reward_Rules.views import (
    Item_Condition_ViewSet,
)
from app_8_Reward_Rules.Views__Files.reward_rule_view import Reward_Rule_ViewSet

# App - 9
from app_9_Reward_Products.Reward_Category__API__1.views import Reward_Category_ViewSet
from app_9_Reward_Products.Reward_Product__API__2.views import Reward_Product_ViewSet
from app_9_Reward_Products.Reward_Product_Images__API__3.views import (
    Reward_Product_Image_ViewSet,
)

# App - 10
from app_10_E_Waste_Submission.E_Waste_Submission__API__1.views import (
    E_Waste_Submission_ViewSet,
)
from app_10_E_Waste_Submission.E_Waste_Status_History__API__3.views import (
    E_Waste_Status_History_ViewSet,
)

# App - 11
from app_11_User_Rewards.User_Rewards__API__1.views import (
    User_Wallet_ViewSet,
    Reward_Transaction_ViewSet,
)

# app-12
from app_12_Reward_Cart.Reward_Cart__API__1.views import (
    Admin_Reward_Cart_ViewSet,
    User_Reward_Cart_ViewSet,
)
from app_12_Reward_Cart.Reward_Cart_Items__API__2.views import (
    Admin_Reward_Cart_Items_ViewSet,
    User_Reward_Cart_Items_ViewSet,
)

# app-13
from app_13_reward_orders.Reward_Order__API__1.views import (
    Admin_Reward_Order_ViewSet,
    User_Reward_Order_ViewSet,
)
from app_13_reward_orders.Reward_Order_Items__API__2.views import (
    Admin_Reward_Order_Item_ViewSet,
)
from app_13_reward_orders.Reward_Order_Address__API__3.views import (
    Admin_Reward_Order_Address_ViewSet,
)
from app_13_reward_orders.Reward_Order_Payment__API__4.views import (
    Admin_Reward_Order_Payment_ViewSet,
)
from app_13_reward_orders.Reward_Order_Status_History__API__5.views import (
    Reward_Order_Status_History_ViewSet,
    User_Reward_Order_Status_History_ViewSet,
)

# app-14
from app_14_reward_returns.Reward_Order_Return_Request__API__1.views import (
    Admin_Reward_Order_Return_Request_ViewSet,
)
from app_14_reward_returns.Reward_Order_Return_Status_History__API__3.views import (
    Admin_Reward_Order_Return_Status_History_ViewSet,
)
from app_14_reward_returns.Reward_Order_Return_Items__API__2.views import (
    Admin_Reward_Order_Return_Item_ViewSet,
)
from app_14_reward_returns.Reward_Order_Return_Pickups__API__4.views import (
    Admin_Reward_Order_Return_Pickup_ViewSet,
)

# app-15
from app_15_reward_replaces.Reward_Order_Replace_Request__API__1.views import (
    Admin_Reward_Order_Replace_Request_ViewSet,
)
from app_15_reward_replaces.Reward_Order_Replace_Status_History__API__3.views import (
    Admin_Reward_Order_Replace_Status_History_ViewSet,
)
from app_15_reward_replaces.Reward_Order_Replace_Items__API__2.views import (
    Admin_Reward_Order_Replace_Item_ViewSet,
)
from app_15_reward_replaces.Reward_Order_Replace_Pickups__API__4.views import (
    Admin_Reward_Order_Replace_Pickup_ViewSet,
)


from django.conf import settings
from django.conf.urls.static import static

# from app_2_e_Facility.DRF__API__app__2__E_Facility.views import RegisterViewSet,LoginView

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create Router Object
router = DefaultRouter()

router.register(
    "1___API__app__1__User_Register", RegisterViewSet, basename="Register_readonly"
)
router.register(
    "1___2___API__app__1__User_Register",
    User_RegisterViewSet,
    basename="User_Register_readonly",
)
router.register(
    "1___3___API__app__1__Admin_User_Register",
    Admin_RegisterViewSet,
    basename="Admin_Register_readonly",
)

router.register(
    "2___API__app__2__Recycling_info",
    Recycle_Admin_View,
    basename="Recycling_info_readonly",
)

router.register(
    "4___API__app__4__Education", Education_view_set, basename="Education_readonly"
)

router.register("5___API__app__5__Home", HowItWorks_ViewSet, basename="Home_readonly")
router.register(
    "5___1___API__app__5__Home", Hero_Section_Admin_ViewSet, basename="Hero_readonly"
)

router.register("6___API__app__6__Brand", Brand_ViewSet, basename="Brands_readonly")


router.register(
    "7___API__app__7__Category_Brand_Mapping",
    Category_Brand_Mapping_ViewSet,
    basename="Category_Brand_Mapping_readonly",
)
router.register(
    "7___1___API__app__7__Product_Model_Name",
    Product_Model_Name_ViewSet,
    basename="Product_Model_Name_readonly",
)


router.register(
    "8___API__app__8__Item_Condition",
    Item_Condition_ViewSet,
    basename="Item_Condition_readonly",
)
router.register(
    "8___1___API__app__8__Reward_Rule",
    Reward_Rule_ViewSet,
    basename="Reward_Rule_readonly",
)

router.register(
    "9___1___API__app__9__Reward_Category",
    Reward_Category_ViewSet,
    basename="Reward_Category_readonly",
)
router.register(
    "9___2___API__app__9__Reward_Product",
    Reward_Product_ViewSet,
    basename="Reward_Product_readonly",
)
router.register(
    "9___3___API__app__9__Reward_Product_Image",
    Reward_Product_Image_ViewSet,
    basename="Reward_Product_Image_readonly",
)

router.register(
    "10___API__app__10__E_Waste_Submission",
    E_Waste_Submission_ViewSet,
    basename="E_Waste_Submission_readonly",
)
router.register(
    "10___2___API__app__10__E_Waste_Status_History",
    E_Waste_Status_History_ViewSet,
    basename="E_Waste_Status_History_readonly",
)

router.register(
    "11___1___API__app__11__User_Wallet",
    User_Wallet_ViewSet,
    basename="User_Wallet_readonly",
)
router.register(
    "11___2___API__app__11__Reward_Transactions",
    Reward_Transaction_ViewSet,
    basename="Reward_Transactions_readonly",
)

# app-12
router.register(
    "12___1___API__app__12__Reward_Cart",
    Admin_Reward_Cart_ViewSet,
    basename="Reward_Cart_readonly",
)

router.register(
    "12___2___API__app__12__Reward_Cart_Items",
    Admin_Reward_Cart_Items_ViewSet,
    basename="Reward_Cart_Items_readonly",
)

# app-13
router.register(
    "13___1___API__app__13__Reward_Order",
    Admin_Reward_Order_ViewSet,
    basename="Reward_Order_admin",
)

router.register(
    "13___2___API__app__13__Reward_Order_Items",
    Admin_Reward_Order_Item_ViewSet,
    basename="Reward_Order_Items_admin",
)

router.register(
    "13___3___API__app__13__Reward_Order_Address",
    Admin_Reward_Order_Address_ViewSet,
    basename="Reward_Order_Address_admin",
)

router.register(
    "13___4___API__app__13__Reward_Order_Payment",
    Admin_Reward_Order_Payment_ViewSet,
    basename="Reward_Order_Payment_admin",
)

router.register(
    "13___5___API__app__13__Reward_Order_Status_History",
    Reward_Order_Status_History_ViewSet,
    basename="Reward_Order_Status_History_admin",
)

router.register(
    "13___5___API__app__13__User_Reward_Order",
    User_Reward_Order_ViewSet,
    basename="User_Reward_Order",
)

router.register(
    "14___1___API__app__14__Admin_Return_Request",
    Admin_Reward_Order_Return_Request_ViewSet,
    basename="Admin_Return_Request",
)

router.register(
    "14___2___API__app__14__Admin_Return_Status_History",
    Admin_Reward_Order_Return_Status_History_ViewSet,
    basename="Admin_Return_Status_History",
)

router.register(
    "14___3___API__app__14__Admin_Return_Item",
    Admin_Reward_Order_Return_Item_ViewSet,
    basename="Admin_Return_Item",
)

router.register(
    "14___4___API__app__14__Admin_Return_Pickup",
    Admin_Reward_Order_Return_Pickup_ViewSet,
    basename="Admin_Return_Pickup",
)

# app-15
router.register(
    "15___1___API__app__15__Admin_Replace_Request",
    Admin_Reward_Order_Replace_Request_ViewSet,
    basename="Admin_Replace_Request",
)

router.register(
    "15___2___API__app__15__Admin_Replace_Status_History",
    Admin_Reward_Order_Replace_Status_History_ViewSet,
    basename="Admin_Replace_Status_History",
)

router.register(
    "15___3___API__app__15__Admin_Replace_Item",
    Admin_Reward_Order_Replace_Item_ViewSet,
    basename="Admin_Replace_Item",
)

router.register(
    "15___4___API__app__15__Admin_Replace_Pickup",
    Admin_Reward_Order_Replace_Pickup_ViewSet,
    basename="Admin_Replace_Pickup",
)


# ------------ sign_up_2 ---------
# router.register('2___API__app__1__User__modelviewset', user_ModelViewSet_2, basename='students_modelviewset__2')


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('app_1_users.urls', namespace='1_app')),  # App's routes
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login__2/", LoginView.as_view(), name="login_api"),
    path("user/login/", UserLoginView.as_view()),
    path("api/admin/login/", AdminLoginView.as_view()),
    # --------------- app - 2
    path("api/", include("app_2_e_Facility.urls")),
    path("User-api/", include("app_2_e_Facility.urls")),
    # --------------- app - 3
    path("api/", include("app_3_Recycling_info.urls")),
    path("User-api/", include("app_3_Recycling_info.urls")),
    # --------------- app - 4
    # ===== Education App =====
    path("User-api/", include("app_4_Education.urls")),
    # --------------- app - 5
    # ===== Home App =====
    path("User-api/", include("app_5_Home.urls")),
    # --------------- app - 6
    # ===== Brands App =====
    path("User-api/", include("app_6_Brands.urls")),
    # --------------- app - 7
    # ===== Category_Brand_Mapping App =====
    path("User-api/", include("app_7_Category_Brand_Mapping.urls")),
    # --------------- app - 8
    # ===== Reward_Rule App =====
    path("User-api/", include("app_8_Reward_Rules.urls")),
    # app-9
    path("User-api/", include("app_9_Reward_Products.urls")),
    # app-10
    path("User-api/", include("app_10_E_Waste_Submission.urls")),
    # app-11
    path("User-api/", include("app_11_User_Rewards.urls")),
    # app-12
    path("User-api/", include("app_12_Reward_Cart.urls")),
    # app-13
    path("User-api/", include("app_13_reward_orders.urls")),
    # app-14
    path("User-api/", include("app_14_reward_returns.urls")),
    # app-15
    path("User-api/", include("app_15_reward_replaces.urls")),
    # log-in (button) show top --> right(side) in Browser
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]


# For serving media files (Image File) globally
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
