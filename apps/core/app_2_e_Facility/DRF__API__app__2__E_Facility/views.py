from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from app_2_e_Facility.models import Facility
from .serializer import FacilitySerializer

# class FacilityListAPIView(APIView):
#     def get(self, request):
#         facilities = Facility.objects.all()
#         serializer = FacilitySerializer(facilities, many=True)
#         return Response(serializer.data)


class FacilityListAPIView(ListAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer