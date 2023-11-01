from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from twilio.rest import Client

from Trufrend.models import Profile,Video,Challenge
from rest_framework import viewsets
from rest_framework import status
from rest_framework import viewsets
from rest_framework import status
import os
import requests


# Load environment variables from .env file
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Trufrend.serializers import ProfileSerializer,VideoSerializer
from django.conf import settings

class InitiateVerificationView(APIView):
    def post(self, request):
        print(request.data)
        ACCOUNT_SID = config('TWILIO_ACCOUNT_SID', default='')
        AUTH_TOKEN = config('TWILIO_AUTH_TOKEN', default='')
        VERIFY_SERVICE_SID = config('TWILIO_VERIFY_SERVICE_SID', default='')
        phone = "+91" + request.data.get('phone')
        if not phone:
            return Response({'error': 'phone number is requied'})
        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            verification = client.verify \
                .services(VERIFY_SERVICE_SID) \
                .verifications \
                .create(to=phone, channel='sms')
            return Response({'message': 'Verification initiated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyUserView(APIView):
    def post(self, request):
        ACCOUNT_SID = config('TWILIO_ACCOUNT_SID', default='')
        AUTH_TOKEN = config('TWILIO_AUTH_TOKEN', default='')
        VERIFY_SERVICE_SID = config('TWILIO_VERIFY_SERVICE_SID', default='')
        print(request.data)
        phone = "+91" + request.data.get('phone')
        code = request.data.get('code')
        print(phone)
        if not phone or not code:
            return Response({'error': 'Phone number and code are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            verification_check = client.verify \
                .services(VERIFY_SERVICE_SID) \
                .verification_checks \
                .create(to=phone, code=code)
            if verification_check.status == 'approved':
                # Create or update user object here
                return Response({'message': 'User verified.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class Nickname(APIView):
    def post(self, request):
        nick_name = request.data.get('nick_name')
         # Assuming you send the profile ID along with nick_name
        profile=Profile.objects.create(nick_name=nick_name)
        profile.save()
        return Response({'message': 'Nick name added'}, status=status.HTTP_200_OK)

class Age(APIView):
    def post(self, request):
        age = request.data.get('age')
        profile_id = request.data.get('profile_id')  # Assuming you send the profile ID along with age

        try:
            profile = Profile.objects.get(id=profile_id)
            profile.age = age
            profile.save()
            return Response({'message': 'Age added'}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)


class AddChallenges(APIView):
    def post(self, request):
        try:
            profile_id = request.data.get('profile_id')  # Change 'id' to 'profile_id'
            challenges_ids = request.data.get('challenges_ids', [])
            # Default to an empty list if not provided

            # Check if the profile_id is a valid number
            if not profile_id :
                return Response({'error': 'Invalid profile ID provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the profile object
            try:
                profile = Profile.objects.get(id=profile_id)
            except Profile.DoesNotExist:
                return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Validate challenge IDs and ensure uniqueness
            valid_challenges = []
            for challenge_id in challenges_ids:
                try:
                    challenge = Challenge.objects.get(id=challenge_id)
                    if challenge not in valid_challenges:  # Ensure uniqueness
                        valid_challenges.append(challenge)
                except Challenge.DoesNotExist:
                    return Response({'error': f'Challenge with ID {challenge_id} not found.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            # Add the unique challenges to the profile using the many-to-many relationship
            profile.challenges.add(*valid_challenges)

            return Response({'message': 'Challenges added to the profile successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateSOS(APIView):
    def post(self, request):
        SOS = request.data.get('SOS')
        id = request.data.get('id')  # Assuming you send the profile ID along with age

        try:
            profile = Profile.objects.get(id=id)
            profile.SOS = SOS
            profile.save()
            return Response({'message': 'SOS added'}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
class UserCount(APIView):
    def get(self,request):
        try:
           user=Profile.objects.count()
           return Response({'user': user}, status=status.HTTP_200_OK)
        except Exception as e:
                print(str(e))  # Log the exception for debugging
                return Response({'error': 'Error occurred while fetching user count.'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
# Create your views here.
