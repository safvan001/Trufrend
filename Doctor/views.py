from django.shortcuts import render

from AdminSide.serializers import  DoctorDataSerializer
from Doctor.serializers import FeedbackSerializer,ScheduleSerilaizer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import generics
from django.utils import timezone
from rest_framework.views import APIView
from Trufrend.models import Profile
from AdminSide.models import DoctorData
from Doctor.models import Feedback,Schedule
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
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
        usernickname=request.data.get('usernickname')
        doctor_username=request.data.get('doctor_username')
        reason=request.data.get('reason')
        time=timezone.now()
        try:
            doctor=DoctorData.objects.get(username=doctor_username)

            feedback = Feedback.objects.create(doctor=doctor,usernickname=usernickname,reason=reason,time=time)
            serializer=FeedbackSerializer(feedback)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DoctorData.DoesNotExist:
            return Response({'error': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request):
        try:
            feedbacks=Feedback.objects.all().order_by('-time')
            serilaizer=FeedbackSerializer(feedbacks,many=True)
            return Response(serilaizer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CounselorScheduling(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        counselor_username = request.data.get('counselor_username')
        message = request.data.get('message')
        date = timezone.now()
        try:
            user = Profile.objects.get(phone_number=phone)
        except Profile.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            counselor = DoctorData.objects.get(username=counselor_username)
        except DoctorData.DoesNotExist:
            return Response({'error': 'Counselor not found.'}, status=status.HTTP_404_NOT_FOUND)

        scheduled = Schedule.objects.create(user=user, counselor=counselor, date=date, message=message)
        serializer = ScheduleSerilaizer(scheduled)

        return Response(serializer.data, status=status.HTTP_200_OK)
class ScheduledCounselor(APIView):

    def get(self,request,counselor_username):
        try:
            doctor=DoctorData.objects.get(username=counselor_username)
            Schedules=Schedule.objects.filter(counselor=doctor)

            serilaizer=ScheduleSerilaizer(Schedules,many=True)

            return Response(serilaizer.data, status=status.HTTP_200_OK)

        except Profile.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
class CounselorReply(APIView):
    def post(self, request, schedule_id):
        try:
            schedule = Schedule.objects.get(id=schedule_id)
        except Schedule.DoesNotExist:
            return Response({'error': 'Schedule not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        counselor_reply = request.data.get('counselor_reply')
        schedule.counselor_reply = counselor_reply
        schedule.save()

        serializer = ScheduleSerializer(schedule)  # Fix the typo here
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetCounselorReply(APIView):

    def get(self, request, phone):
        try:
            profile = Profile.objects.get(phone_number=phone)
            Schedules = Schedule.objects.filter(user=profile)

            serilaizer = ScheduleSerilaizer(Schedules, many=True)

            return Response(serilaizer.data, status=status.HTTP_200_OK)

        except Profile.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)



























