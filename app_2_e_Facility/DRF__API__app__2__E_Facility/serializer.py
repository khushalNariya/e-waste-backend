from rest_framework import serializers
from app_2_e_Facility.models import Facility

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'
