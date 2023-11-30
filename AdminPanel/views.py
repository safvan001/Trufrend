from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from AdminPanel.models import Upload,DoctorDetail
from AdminPanel.serializers import UploadSerializer,DoctorDetailSerializer,UserSerializer

class SampleUpload(generics.ListCreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
class AddDoctorView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class DoctordetailView(generics.ListCreateAPIView):
    queryset=DoctorDetail.objects.all()
    serializer_class = DoctorDetailSerializer

# Create your views here.
