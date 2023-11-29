from django.shortcuts import render
from rest_framework import generics
from AdminPanel.models import Upload
from AdminPanel.serializers import UploadSerializer

class SampleUpload(generics.ListCreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
# Create your views here.
