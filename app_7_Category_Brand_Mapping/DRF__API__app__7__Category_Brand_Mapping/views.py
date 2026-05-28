from rest_framework.viewsets import ModelViewSet
from app_7_Category_Brand_Mapping.models import Category_Brand_Mapping_Model
from .serializer import Category_Brand_Mapping_Serializer

from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.authentication import SessionAuthentication

# --- Pagination
from .pagination import user__Pagination  # ---- import (pagination.py) file
from rest_framework.permissions import IsAdminUser,IsAuthenticated

# ===========================================================================
# ======================== Category_Brand_Mapping (Admin) Interface ========================
# ===========================================================================
class Category_Brand_Mapping_ViewSet(ModelViewSet):
    queryset = Category_Brand_Mapping_Model.objects.all()
    serializer_class = Category_Brand_Mapping_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser] # is_staf = true, is_active = true

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "category__title",
        "brand__name"

    ]

    pagination_class = user__Pagination  # ---- import (pagination.py) file

## Filter (Category wise Brand ) Fatch

    # def filter_queryset(self, queryset):
    #     search_param = self.request.query_params.get('search', None)
    #     # Custom logic to handle frontend sending `search=category_id=X`
    #     if search_param and search_param.startswith('category_id='):
    #         try:
    #             cat_id = int(search_param.split('=')[1])
    #             return queryset.filter(category_id=cat_id)
    #         except ValueError:
    #             pass
        
    #     return super().filter_queryset(queryset)



# ===========================================================================
# ======================== Category_Brand_Mapping (User/Public) Interface ========================
# ===========================================================================
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class Category_Brand_Public_View(ListAPIView):
    queryset = Category_Brand_Mapping_Model.objects.filter(is_active=True)
    serializer_class = Category_Brand_Mapping_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



# ===========================================================================
# ======================== Category_Brand_Mapping (Api) ========================
# ===========================================================================
# =========================Category wise Brand (Filter) Admin -Side (Category - Wise - Brand - (Fatch) + Model Name Add (ex. samsung s26 , vivo v60))==================================================
# ===========================================================================

class Category_Brand_Filter_View(ListAPIView):
    queryset = Category_Brand_Mapping_Model.objects.filter(is_active=True)
    serializer_class = Category_Brand_Mapping_Serializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        category_id = self.request.query_params.get("category_id")

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset
