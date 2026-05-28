from rest_framework.viewsets import ModelViewSet
from app_7_Category_Brand_Mapping.models import Product_Model_Name_Model
from app_7_Category_Brand_Mapping.Product__Model__Name____API.product__Model___Serializer import (
    Product_Model_Name_Serializer,
)

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView
from app_7_Category_Brand_Mapping.models import Category_Brand_Mapping_Model
from app_7_Category_Brand_Mapping.DRF__API__app__7__Category_Brand_Mapping.pagination import (
    user__Pagination,
)


class Product_Model_Name_ViewSet(ModelViewSet):
    queryset = Product_Model_Name_Model.objects.all().order_by("-id")
    serializer_class = Product_Model_Name_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]  # is_staf = true, is_active = true

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["category__title", "brand__name", "model_name"]

    pagination_class = user__Pagination  # ---- import (pagination.py) file





# ===========================================================================
# ======================== Product_Model_Name (Api) ========================
# ===========================================================================
# =========================Category wise Brand wise Model (Filter) Admin -Side (Category - Wise - Brand (Fatch) + (Brand ) Wise ( Model Name) Fatch ==================================================
# ===========================================================================

# Is view ko views.py mein niche add karein
class Product_Model_Filter_View(ListAPIView):
    serializer_class = Product_Model_Name_Serializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        mapping_id = self.request.query_params.get("category_brand_mapping_id")
        if mapping_id:
            try:
                # Pehle mapping se category aur brand nikaalein
                mapping = Category_Brand_Mapping_Model.objects.get(id=mapping_id)
                # Phir unke base par models filter karein
                return Product_Model_Name_Model.objects.filter(
                    category=mapping.category, 
                    brand=mapping.brand,
                    is_active=True
                )
            except Category_Brand_Mapping_Model.DoesNotExist:
                return Product_Model_Name_Model.objects.none()
        return Product_Model_Name_Model.objects.none()
