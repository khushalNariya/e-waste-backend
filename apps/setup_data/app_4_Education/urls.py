from django.urls import path
from app_4_Education.DRF__API__app__4__Education.views import EducationListAPIView, EducationDetailAPIView

urlpatterns = [
    path("education/", EducationListAPIView.as_view()),
    path("education/<slug:slug>/", EducationDetailAPIView.as_view()),


]
