from rest_framework import serializers
from AdminSide.models import DoctorData,Quotes,Languages,Specality,Stories


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Languages
        fields='__all__'
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Specality
        fields='__all__'

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = '__all__'   #['id', 'story_file', 'created_at', 'media_type']
class DoctorDataSerializer(serializers.ModelSerializer):
    from Trufrend.serializers import VideoSerializer
    Language=LanguageSerializer(many=True)
    Specialization=SpecializationSerializer(many=True)
    VideoFavour=VideoSerializer(many=True)
    story=StoriesSerializer(many=True)
    class Meta:
        model=DoctorData
        fields='__all__'
from django.http import JsonResponse
# class StoriesSerializer(serializers.ModelSerializer):
#     doctor=DoctorDataSerializer()
#     class Meta:
#         model = Stories
#         fields = '__all__'


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quotes
        fields='__all__'





