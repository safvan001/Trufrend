from rest_framework import serializers
from AdminSide.models import DoctorData,Languages,Specality

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Languages
        fields='__all__'
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Specality
        fields='__all__'
class DoctorDataSerializer(serializers.ModelSerializer):
    Language=LanguageSerializer(many=True)
    Specialization=SpecializationSerializer(many=True)
    class Meta:
        model=DoctorData
        fields='__all__'



