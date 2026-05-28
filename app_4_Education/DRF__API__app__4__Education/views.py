from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from app_4_Education.models import EducationArticle_model
from .serializer import Education_Serializer
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
# --- Pagination
from .pagination import user__Pagination  # ---- import (pagination.py) file



# ========= Admin - Interface ================

class Education_view_set(ModelViewSet):

        queryset  = EducationArticle_model.objects.all().order_by('-id')
        serializer_class  = Education_Serializer
        parser_classes = [MultiPartParser, FormParser]
        authentication_classes = [JWTAuthentication]


# ---------- Combine All Filters -----------
        filter_backends = [SearchFilter, OrderingFilter]
        search_fields = [
        "title",
        "category",
        "readTime",
         ]

        pagination_class = user__Pagination  # ---- import (pagination.py) file

        
        def update(self, request, *args, **kwargs):
                partial = kwargs.pop('partial', True)
                instance = self.get_object()
                serializer = self.get_serializer(
                        instance,
                        data=request.data,
                        partial=partial
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)


# ========= User - Interface ================
class EducationListAPIView(ListAPIView):

        queryset  = EducationArticle_model.objects.all().order_by('-id')
        serializer_class  = Education_Serializer
        # lookup_field = "id"


class EducationDetailAPIView(RetrieveAPIView):
    queryset = EducationArticle_model.objects.all()
    serializer_class = Education_Serializer
    lookup_field = "slug"