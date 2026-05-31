from django.contrib import admin
from django.urls import path, include
from app_1_users.DRF__API__app__1__users.views import user_ModelViewSet
from rest_framework.routers import DefaultRouter

# Create Router Object
router = DefaultRouter()

# Register Student_ViewSet
router.register('1_students_modelviewset', user_ModelViewSet, basename='students_modelviewset')
# router.register('2_students_readonly_modelviewset', Student_ModelViewSet, basename='students_readonly')

urlpatterns = [

    path('', include(router.urls)),

# log-in (button) show top --> right(side) in Browser
        path('basic_authentaction/', include('rest_framework.urls' , namespace="rest_framework")),

        # path('', include('app__17__3.urls')), # <-- include app's urls here

        
]
