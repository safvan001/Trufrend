from django.shortcuts import render
from rest_framework import generics
from AdminSide.models import DoctorData
from rest_framework.views import APIView
from AdminSide.serializers import  DoctorDataSerializer
from rest_framework.response import Response
from rest_framework import status

class DoctorDataView(generics.ListCreateAPIView):
    queryset = DoctorData.objects.all()
    serializer_class =  DoctorDataSerializer

# class DoctordatView(APIView):
#     def post(self,request):
#         username=request.data.get('username')
#         password=request.data.get('password')
#         DOB=request.data.get('DOB')
#         CurrentAddress=request.data.get('CurrentAddress')
#         permanentAddress=request.data.get('permanentAddress')
#         phone=request.data.get('phone')
#         Degrees=request.data.get('Degrees')
#         Diplomas=request.data.get('Diplomas')
#         References=request.data.get('References')
#         Certificates=request.data.get('Certificates')
#         RCI=request.data.get('RCI')
#         PAN=request.data.get('PAN')
#         Aadhaar=request.data.get('Aadhaar')
#         GST=request.data.get('GST')
#         Aboutme=request.data.get('Aboutme')
#         Education=request.data.get('Education')
#         Experience=request.data.get('Experience')
#         callDuration=request.data.get('callDuration')
#         try:
#             DoctorData.objects.create(username=username,password=password,DOB=DOB,CurrentAddress=CurrentAddress,
#                                       permanentAddress=permanentAddress,phone=phone,Degrees=Degrees,Diplomas= Diplomas,
#                                       References=References,Certificates=Certificates,RCI=RCI,PAN=PAN,Aadhaar=Aadhaar,
#                                       GST=GST,Aboutme=Aboutme,Education=Education,Experience=Experience,callDuration=callDuration)
#             DoctorData.save()
#         except:
#             return Response({'error': 'Wrong Input'}, status=status.HTTP_404_NOT_FOUND)

        # Create your views here.
