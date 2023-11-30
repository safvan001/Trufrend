from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from AdminPanel.models import Upload,DoctorDetail,Language,Specialty
from AdminPanel.serializers import UploadSerializer,DoctorDetailSerializer,UserSerializer,LanguageSerializer,SpecialtySerializer
from rest_framework.response import Response
class SampleUpload(generics.ListCreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
class AddDoctorView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class DoctordetailView(generics.ListCreateAPIView):
    queryset=DoctorDetail.objects.all()
    serializer_class = DoctorDetailSerializer

    # def list(self, request, *args, **kwargs):
    #
    #     # Add details of languages and specializations to the response
    #     languages = Language.objects.all()
    #     specialties = Specialty.objects.all()
    #     Doctor_detail= DoctorDetail.objects.all()
    #
    #     language_serializer = LanguageSerializer(languages, many=True)
    #     specialty_serializer = SpecialtySerializer(specialties, many=True)
    #     Doctor_DetailSerializer=DoctorDetailSerializer(Doctor_detail,many=True)
    #     response_data = {
    #         "languages": language_serializer.data,
    #         "specialties": specialty_serializer.data,
    #         "Doctor_detail": Doctor_DetailSerializer.data,
    #     }
    #
    #     return Response(response_data)

# Create your views here.
