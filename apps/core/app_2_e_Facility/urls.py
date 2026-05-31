from django.urls import path
from app_2_e_Facility.DRF__API__app__2__E_Facility.views import FacilityListAPIView

urlpatterns = [
    # path('facilities/', FacilityListAPIView.as_view(), name='facility-list'),
        path("facilities/", FacilityListAPIView.as_view()),

]
