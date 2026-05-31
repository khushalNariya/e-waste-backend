from django.urls import path
from .E_Waste_Submission__API__1.views import User_EWaste_Submission_ViewSet
from .E_Waste_Status_History__API__3.views import User_EWaste_Status_History_ViewSet

urlpatterns = [
    # =========================
    # User URLS
    path(
        "E-wast-submission/", User_EWaste_Submission_ViewSet.as_view({"get": "list", "post": "create"})
    ),
    path(
        "E-wast-status-history/", User_EWaste_Status_History_ViewSet.as_view({"get": "list"})
    ),
    # =========================
]
