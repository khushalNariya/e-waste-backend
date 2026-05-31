from django.urls import path
from app_6_Brands.DRF__API__app__6__Brands.views import All_Brand_Fatch_ViewSet


urlpatterns = [

    path('all-brand-show/', All_Brand_Fatch_ViewSet.as_view(), name='all-brand'),

]