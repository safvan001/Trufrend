from rest_framework import serializers
from AdminSide.models import DoctorData,Stories,Quotes,Languages,Specality #Languages,Specality

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
    # story=StoriesSerializer()
    class Meta:
        model=DoctorData
        fields='__all__'
from django.http import JsonResponse
class StoriesSerializer(serializers.ModelSerializer):
    doctor=DoctorDataSerializer()
    class Meta:
        model = Stories
        fields = '__all__'


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quotes
        fields='__all__'





