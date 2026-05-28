from django.urls import path
from app_5_Home.DRF__API__app__5__Home.views import HowItWorks_Public_View,Hero_Section_Public_View

urlpatterns = [
    path("how-it-works/", HowItWorks_Public_View.as_view()),

    path("Hero/", Hero_Section_Public_View.as_view()),
]
