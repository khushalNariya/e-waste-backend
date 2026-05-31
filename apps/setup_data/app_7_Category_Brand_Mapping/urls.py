from django.urls import path
from app_7_Category_Brand_Mapping.DRF__API__app__7__Category_Brand_Mapping.views import (
    Category_Brand_Public_View,
    Category_Brand_Filter_View,
)

from app_7_Category_Brand_Mapping.Product__Model__Name____API.product__Model___View import (
    Product_Model_Filter_View,
)

# from app_7_Category_Brand_Mapping.Product__Model__Name____API.product__Model___View import (
#     Product_Model_Name_Public_View,
# )

urlpatterns = [
    # Category Brand (Url)
    path("Category_Brand/", Category_Brand_Public_View.as_view()),
    # Category Wise Brand (Filter) (Url)
    path("Category_Wise_Brand_Filter/", Category_Brand_Filter_View.as_view()),

    # Category Wise Brand Wise Model (Filter) Admin -Side (Category - Wise - Brand (Fatch) + (Brand ) Wise ( Model Name) Fatch (ex. Samsung S26 , Vivo V60))
    path("Category_Wise_Brand_Wise_Model_Filter/", Product_Model_Filter_View.as_view()),
]
