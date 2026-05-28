# views.py

from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from .models import Reward_Product_Image_model
from .serializers import Reward_Product_Image_Serializer

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# pagi
from ..Pagination__File.pagination import user__Pagination


class Reward_Product_Image_ViewSet(ModelViewSet):

    # queryset = Reward_Product_Image_model.objects.all().order_by('product_id','-is_primary','display_order')
    queryset = Reward_Product_Image_model.objects.all().order_by('product_id','display_order')
    serializer_class = Reward_Product_Image_Serializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = [
        "product__name",
    ]

    ordering_fields = ["id", "display_order", "created_at"]

    pagination_class = user__Pagination

    # Partial update support
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super().get_queryset()

        product_id = self.request.query_params.get("product_id")

        if product_id:
            queryset = queryset.filter(product_id=product_id)

        return queryset