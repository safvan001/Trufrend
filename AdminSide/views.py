from django.shortcuts import render
from rest_framework import generics
from AdminSide.models import DoctorData
from AdminSide.serializers import  DoctorDataSerializer


class DoctorDataView(generics.ListCreateAPIView):
    queryset = DoctorData.objects.all()
    serializer_class =  DoctorDataSerializer
# Create your views here.
