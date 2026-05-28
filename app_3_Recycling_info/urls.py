from django.urls import path
from app_3_Recycling_info.DRF__API__app__3__Recycling_info.views import Recycle_ListAPIView,All_Recycle_Category_Fatch_View

urlpatterns = [

        # Recycle Category (Public) 
        path("recycle/", Recycle_ListAPIView.as_view()),
        
        # All Recycle Category (Admin - side) Droup-Down (all - Data - fatch) 
        path("all-recycle-category/", All_Recycle_Category_Fatch_View.as_view()),

]
