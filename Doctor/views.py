from django.shortcuts import render

from AdminSide.serializers import  DoctorDataSerializer
from Doctor.serializers import FeedbackSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import generics
from django.utils import timezone
from rest_framework.views import APIView
from Trufrend.models import Profile
from AdminSide.models import DoctorData
from Doctor.models import Feedback
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class DoctorLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # print(f"Username: {username}, Password: {password}")

        if not username or not password:
            return Response({'detail': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            doctor = DoctorData.objects.get(username=username)
            # print(f"Stored Password: {doctor.password}")
        except DoctorData.DoesNotExist:
            return Response({'detail': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        if password == doctor.password:
            # Serialize the doctor data
            serializer = DoctorDataSerializer(doctor)
            serialized_data = serializer.data

            # Include the serialized data in the response
            response_data = {
                'detail': 'Authentication successful',
                'user_id': doctor.id,
                'doctor_data': serialized_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({'detail': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
class DoctorFeedback(APIView):
    def post(self,request):
        doctor_username=request.data.get('doctor_username')
        reason=request.data.get('reason')
        try:
            doctor=DoctorData.objects.get(username=doctor_username)

            feedback = Feedback.objects.create(doctor=doctor,reason=reason)
            serializer=FeedbackSerializer(feedback)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DoctorData.DoesNotExist:
            return Response({'error': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request):
        try:
            feedbacks=Feedback.objects.all()
            serilaizer=FeedbackSerializer(feedbacks,many=True)
            return Response(serilaizer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)