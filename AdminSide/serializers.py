from rest_framework import serializers
from AdminSide.models import DoctorData


class DoctorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorData
        fields='__all__'



