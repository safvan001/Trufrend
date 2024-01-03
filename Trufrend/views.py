from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from twilio.rest import Client
from django.utils import timezone
from Trufrend.models import Profile,Video,Challenge,VideoPack,Favorite,ContactUs,Rating,Usercount,Languages,Recent
from AdminSide.models import DoctorData

from django.contrib.auth.models import User
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
from rest_framework import generics,mixins
from Trufrend.serializers import ProfileSerializer,VideoSerializer,VideoPackSerializer,ChallengeSerializer,DpSerializer,FavoriteProfileSerializer,ContactSerializer,RatingSerializer,OnlineUserCountSerializer,RecentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from django.conf import settings

class InitiateVerificationView(APIView):
    def post(self, request):
        #print(request.data)
        ACCOUNT_SID = config('TWILIO_ACCOUNT_SID', default='')
        AUTH_TOKEN = config('TWILIO_AUTH_TOKEN', default='')
        VERIFY_SERVICE_SID = config('TWILIO_VERIFY_SERVICE_SID', default='')
        # country_code=request.data.get('country_code')
        phone = request.data.get('phone')
        profile, created = Profile.objects.get_or_create(phone_number=phone)
        profile.save()
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
        #print(request.data)
        phone = request.data.get('phone')
        code = request.data.get('code')
        # print(phone)
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


class UserUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class Dp(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = DpSerializer


class Nickname(APIView):
    def post(self, request):
        nick_name = request.data.get('nick_name')
        phone = request.data.get('phone')
         # Assuming you send the profile ID along with nick_name
        try:
            profile = Profile.objects.get(phone_number=phone)
            profile.nick_name = nick_name
            profile.save()
            return Response({'message': 'Nick name added'}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error': 'Phone number not found'}, status=status.HTTP_404_NOT_FOUND)
        # profile=Profile.objects.create(nick_name=nick_name)
        # profile.save()
        # return Response({'message': 'Nick name added'}, status=status.HTTP_200_OK)
class ChallengeList(generics.ListAPIView):
    queryset=Challenge.objects.all()
    serializer_class=ChallengeSerializer
class AddChallenges(APIView):
    def post(self, request):
        try:
            phone = request.data.get('phone')  # Change 'id' to 'profile_id'
            challenges_ids = request.data.get('challenges_ids', [])
            # Default to an empty list if not provided

            if not challenges_ids:
                return Response({'error': 'challenges_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the profile_id is a valid number
            if not phone :
                return Response({'error': 'phone provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the profile object
            try:
                profile = Profile.objects.get(phone_number=phone)
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


class Videotitle(generics.ListCreateAPIView):
    queryset = VideoPack.objects.all()
    serializer_class = VideoPackSerializer

from rest_framework.decorators import action
# views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework import status, parsers


class ProfileListCreateAPIView(APIView):
    # queryset = Profile.objects.all()
    # serializer_class = ProfileSerializer

    def post(self, request):
        phone = request.data.get('phone')
        nick_name = request.data.get('nick_name')
        name = request.data.get('name')
        dp=request.data.get('dp')
        # DOB=request.data.get('DOB')
        Gender=request.data.get('Gender')
        challenges=request.data.get('challenges',[])
        language=request.data.get('language',[])
        videoFavour=request.data.get('videoFavour',[])

        try:
            profile = Profile.objects.get(phone_number=phone)
            profile.nick_name = nick_name
            profile.name = name
            # profile.DOB=DOB
            profile.Gender=Gender
            profile.challenges.add(*challenges)
            profile.language.add(*language)
            profile.videoFavour.add(*videoFavour)

            # If an image is provided, save it to the 'dp' field
            if dp:
                profile.dp = dp

            profile.save()

            return Response({'message': 'User profile updated successfully'}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile Does not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self,request):
        try:
            profile= Profile.objects.all()

            # Serialize the data
            serializer = ProfileSerializer(profile, many=True)

            # Return the serialized data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class AddLanguage(APIView):
    def post(self,request):
        try:
            phone=request.data.get('phone')
            Language_ids = request.data.get('Language_ids', [])

            if not Language_ids:
                return Response({'error': 'Language_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)
            if not phone:
                return Response({'error': 'phone not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                profile = Profile.objects.get(phone_number=phone)
            except Profile.DoesNotExist:
                return Response({'error': 'profile not found.'}, status=status.HTTP_404_NOT_FOUND)

            valid_languages = []
            for language_id in Language_ids:
                try:
                    language = Languages.objects.get(id=language_id)
                    if language not in valid_languages:  # Ensure uniqueness
                        valid_languages.append(language)
                except Languages.DoesNotExist:
                    return Response({'error': f'Languages with ID {language_id} not found.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            # Add the unique challenges to the profile using the many-to-many relationship
            profile.language.add(*valid_languages)

            return Response({'message': 'Language added to the profile successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddVideoFavouriteView(APIView):
    def post(self,request):
        try:
            phone = request.data.get('phone')  # Change 'id' to 'profile_id'
            video_ids = request.data.get('video_ids', [])
            # Default to an empty list if not provided

            if not video_ids:
                return Response({'error': 'video_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the profile_id is a valid number
            if not phone:
                return Response({'error': 'phone provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the profile object
            try:
                profile = Profile.objects.get(phone_number=phone)
            except Profile.DoesNotExist:
                return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Validate challenge IDs and ensure uniqueness
            valid_video = []
            for video_id in video_ids:
                try:
                    video = Video.objects.get(id=video_id)
                    if video not in valid_video:  # Ensure uniqueness
                        valid_video.append(video)
                except Video.DoesNotExist:
                    return Response({'error': f'Video with ID {video_id} not found.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            # Add the unique challenges to the profile using the many-to-many relationship
            profile.videoFavour.add(*valid_video)

            return Response({'message': 'VideoFavourite added to the profile successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DeleteVideoFavouriteView(APIView):
    def post(self, request):
        try:
            phone = request.data.get('phone')  # Change 'id' to 'profile_id'
            video_ids = request.data.get('video_ids', [])

            if not phone or not video_ids:
                return Response({'error': 'Invalid input data.'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the profile object
            try:
                profile = Profile.objects.get(phone_number=phone)
            except Profile.DoesNotExist:
                return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Validate video IDs
            valid_video_ids = [video_id for video_id in video_ids if Video.objects.filter(id=video_id).exists()]

            # Remove the specified videos from the profile's videoFavour
            profile.videoFavour.remove(*valid_video_ids)

            return Response({'message': 'VideoFavourite removed from the profile successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class AddDoctorFavourite(APIView):
#     def post(self,request):
#         try:
#             phone = request.data.get('phone')  # Change 'id' to 'profile_id'
#             doctor_ids = request.data.get('doctor_ids', [])
#             # Default to an empty list if not provided
#
#             if not doctor_ids:
#                 return Response({'error': 'doctor_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             # Check if the profile_id is a valid number
#             if not phone:
#                 return Response({'error': 'phone provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             # Get the profile object
#             try:
#                 profile = Profile.objects.get(phone_number=phone)
#             except Profile.DoesNotExist:
#                 return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#             # Validate challenge IDs and ensure uniqueness
#             valid_doctor = []
#             for doctor_id in doctor_ids:
#                 try:
#                     doctor = DoctorData.objects.get(id=doctor_id)
#                     if doctor not in valid_doctor:  # Ensure uniqueness
#                         valid_doctor.append(doctor)
#                 except DoctorData.DoesNotExist:
#                     return Response({'error': f'Doctor with ID {doctor_id} not found.'},
#                                     status=status.HTTP_400_BAD_REQUEST)
#
#             # Add the unique challenges to the profile using the many-to-many relationship
#             profile.doctorFavour.add(*valid_doctor)
#
#             return Response({'message': 'DoctorFavourite added to the profile successfully.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(str(e))  # Log the exception for debugging
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class RemoveDoctorFavourite(APIView):
#     def post(self, request):
#         try:
#             phone = request.data.get('phone')  # Change 'id' to 'profile_id'
#             doctor_ids = request.data.get('doctor_ids', [])
#
#             if not doctor_ids:
#                 return Response({'error': 'doctor_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             if not phone:
#                 return Response({'error': 'phone not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             try:
#                 profile = Profile.objects.get(phone_number=phone)
#             except Profile.DoesNotExist:
#                 return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#             # Validate doctor IDs and ensure they exist in the favorites list
#             for doctor_id in doctor_ids:
#                 try:
#                     doctor = DoctorData.objects.get(id=doctor_id)
#                     if doctor in profile.doctorFavour.all():
#                         profile.doctorFavour.remove(doctor)
#                     else:
#                         return Response({'error': f'Doctor with ID {doctor_id} is not in favorites.'},
#                                         status=status.HTTP_400_BAD_REQUEST)
#                 except DoctorData.DoesNotExist:
#                     return Response({'error': f'Doctor with ID {doctor_id} not found.'},
#                                     status=status.HTTP_400_BAD_REQUEST)
#
#             return Response({'message': 'Doctor removed from favorites successfully.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(str(e))  # Log the exception for debugging
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class RecentCallsofUser(APIView):
#     def post(self,request):
#         try:
#             phone = request.data.get('phone')  # Change 'id' to 'profile_id'
#             doctor_ids = request.data.get('doctor_ids', [])
#             # Default to an empty list if not provided
#
#             if not doctor_ids:
#                 return Response({'error': 'doctor_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             # Check if the profile_id is a valid number
#             if not phone:
#                 return Response({'error': 'phone provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             # Get the profile object
#             try:
#                 profile = Profile.objects.get(phone_number=phone)
#             except Profile.DoesNotExist:
#                 return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#             # Validate challenge IDs and ensure uniqueness
#             valid_doctor = []
#             for doctor_id in doctor_ids:
#                 try:
#                     doctor = DoctorData.objects.get(id=doctor_id)
#                     if doctor not in valid_doctor:  # Ensure uniqueness
#                         valid_doctor.append(doctor)
#                 except DoctorData.DoesNotExist:
#                     return Response({'error': f'Doctor with ID {doctor_id} not found.'},
#                                     status=status.HTTP_400_BAD_REQUEST)
#
#             # Add the unique challenges to the profile using the many-to-many relationship
#             profile.recent_calls.add(*valid_doctor)
#
#             return Response({'message': 'Recent Calls added to the profile successfully.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(str(e))  # Log the exception for debugging
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class RemoveFromRecent(APIView):
#     def post(self, request):
#         try:
#             phone = request.data.get('phone')  # Change 'id' to 'profile_id'
#             doctor_ids = request.data.get('doctor_ids', [])
#
#             if not doctor_ids:
#                 return Response({'error': 'doctor_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             if not phone:
#                 return Response({'error': 'phone not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             try:
#                 profile = Profile.objects.get(phone_number=phone)
#             except Profile.DoesNotExist:
#                 return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#             # Validate doctor IDs and ensure they exist in the favorites list
#             for doctor_id in doctor_ids:
#                 try:
#                     doctor = DoctorData.objects.get(id=doctor_id)
#                     if doctor in profile.recent_calls.all():
#                         profile.recent_calls.remove(doctor)
#                     else:
#                         return Response({'error': f'Doctor with ID {doctor_id} is not in favorites.'},
#                                         status=status.HTTP_400_BAD_REQUEST)
#                 except DoctorData.DoesNotExist:
#                     return Response({'error': f'Doctor with ID {doctor_id} not found.'},
#                                     status=status.HTTP_400_BAD_REQUEST)
#
#             return Response({'message': 'Doctor removed from Recent Calls successfully.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(str(e))  # Log the exception for debugging
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddDoctorFavourite(APIView):
    def post(self, request):
        try:
            phone = request.data.get('phone')
            doctor_username = request.data.get('doctor_username')

            # Default to an empty list if not provided
            if not doctor_username:
                return Response({'error': 'doctor_username not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the phone is provided
            if not phone:
                return Response({'error': 'phone not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the profile object
            try:
                profile = Profile.objects.get(phone_number=phone)
            except Profile.DoesNotExist:
                return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Validate doctor username and ensure uniqueness
            try:
                doctor = DoctorData.objects.get(username=doctor_username)
            except DoctorData.DoesNotExist:
                return Response({'error': f'Doctor with Username {doctor_username} not found.'}, status=status.HTTP_400_BAD_REQUEST)

            # Add the unique doctor to the profile using the many-to-many relationship
            profile.doctorFavour.add(doctor)

            return Response({'message': 'DoctorFavourite added to the profile successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class RemoveDoctorFavourite(APIView):
    def post(self, request):
        try:
            phone = request.data.get('phone')
            doctor_username = request.data.get('doctor_username')

            if not doctor_username:
                return Response({'error': 'doctor_username not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            if not phone:
                return Response({'error': 'phone not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                profile = Profile.objects.get(phone_number=phone)
            except Profile.DoesNotExist:
                return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Validate doctor IDs and ensure they exist in the favorites list
            try:
                doctor = DoctorData.objects.get(username=doctor_username)
                if doctor in profile.doctorFavour.all():
                    profile.doctorFavour.remove(doctor)
                    return Response({'message': f'Doctor {doctor_username} removed from favorites successfully.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': f'Doctor {doctor_username} is not in favorites.'}, status=status.HTTP_400_BAD_REQUEST)
            except DoctorData.DoesNotExist:
                return Response({'error': f'Doctor with Username {doctor_username} not found.'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class RecentCallsofUser(APIView):
#     def post(self,request):
#         try:
#             phone = request.data.get('phone')  # Change 'id' to 'profile_id'
#             doctor_ids = request.data.get('doctor_ids', [])
#             # Default to an empty list if not provided
#             if not doctor_ids:
#                 return Response({'error': 'doctor_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             # Check if the profile_id is a valid number
#             if not phone:
#                 return Response({'error': 'phone provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             # Get the profile object
#             try:
#                 profile = Profile.objects.get(phone_number=phone)
#             except Profile.DoesNotExist:
#                 return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#             # Validate challenge IDs and ensure uniqueness
#             valid_doctor = []
#             for doctor_id in doctor_ids:
#                 try:
#                     doctor = DoctorData.objects.get(id=doctor_id)
#                     if doctor not in valid_doctor:  # Ensure uniqueness
#                         valid_doctor.append(doctor)
#                 except DoctorData.DoesNotExist:
#                     return Response({'error': f'Doctor with ID {doctor_id} not found.'},
#                                     status=status.HTTP_400_BAD_REQUEST)
#
#             # Add the unique challenges to the profile using the many-to-many relationship
#             profile.recent_calls.add(*valid_doctor)
#
#             return Response({'message': 'Recent Calls added to the profile successfully.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(str(e))  # Log the exception for debugging
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class RemoveFromRecent(APIView):
#     def post(self, request):
#         try:
#             phone = request.data.get('phone')  # Change 'id' to 'profile_id'
#             doctor_ids = request.data.get('doctor_ids', [])
#
#             if not doctor_ids:
#                 return Response({'error': 'doctor_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             if not phone:
#                 return Response({'error': 'phone not provided.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             try:
#                 profile = Profile.objects.get(phone_number=phone)
#             except Profile.DoesNotExist:
#                 return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#             # Validate doctor IDs and ensure they exist in the favorites list
#             for doctor_id in doctor_ids:
#                 try:
#                     doctor = DoctorData.objects.get(id=doctor_id)
#                     if doctor in profile.recent_calls.all():
#                         profile.recent_calls.remove(doctor)
#                     else:
#                         return Response({'error': f'Doctor with ID {doctor_id} is not in favorites.'},
#                                         status=status.HTTP_400_BAD_REQUEST)
#                 except DoctorData.DoesNotExist:
#                     return Response({'error': f'Doctor with ID {doctor_id} not found.'},
#                                     status=status.HTTP_400_BAD_REQUEST)
#
#             return Response({'message': 'Doctor removed from Recent Calls successfully.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(str(e))  # Log the exception for debugging
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetUserCountView(APIView):
    def get(self, request):
        try:
            # Get the existing Usercount instance or create a new one
            user_count_instance, created = Usercount.objects.get_or_create(pk=1, defaults={'user_count': 0})

            return Response({'user_count': user_count_instance.user_count}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class WellnessVideos(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# class GetProfilesByDoctor(APIView):
#     def get(self, request, doctor_username):
#         try:
#             # Filter DoctorData instances based on the username
#             matching_doctors = DoctorData.objects.filter(username=doctor_username)
#
#             if not matching_doctors.exists():
#                 return Response({'error': 'Doctor not found for the given username'}, status=status.HTTP_404_NOT_FOUND)
#
#             # Fetch profiles that have called the doctor from the Recent model
#             calling_profiles = Recent.objects.filter(doctor__in=matching_doctors).values('profile')
#
#             # Extract the profile IDs from the query result
#             profile_ids = calling_profiles.values_list('profile', flat=True)
#
#             # Retrieve the Profile instances based on the profile IDs
#             profiles = Profile.objects.filter(id__in=profile_ids)
#
#             # Serialize the profiles
#             serializer = ProfileSerializer(profiles, many=True)
#
#             return Response({'profiles': serializer.data}, status=status.HTTP_200_OK)
#
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
from collections import Counter

class GetRecentProfile(APIView):
    def get(self, request, doctor_username):
        try:
            # Filter DoctorData instances based on the username
            matching_doctors = DoctorData.objects.filter(username=doctor_username)

            if not matching_doctors.exists():
                return Response({'error': 'Doctor not found for the given username'}, status=status.HTTP_404_NOT_FOUND)

            # Fetch profiles that have called the doctor from the Recent model
            calling_profiles = Recent.objects.filter(doctor__in=matching_doctors)

            # Extract the profile instances from the query result
            profiles = [recent.profile for recent in calling_profiles]

            # Duplicate phone numbers based on the number of occurrences in the result set
            profiles_data = [
                {
                    'user_id': profile.id,
                    'nick_name': profile.nick_name,
                    'time': recent.time,
                }
                for profile, recent in zip(profiles, calling_profiles)
            ]

            return Response(profiles_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



# class GetRecentProfile(APIView):
#     def get(self, request, doctor_username):
#         try:
#             # Filter DoctorData instances based on the username
#             matching_doctors = DoctorData.objects.filter(username=doctor_username)
#
#             if not matching_doctors.exists():
#                 return Response({'error': 'Doctor not found for the given username'}, status=status.HTTP_404_NOT_FOUND)
#
#             # Fetch profiles that have called the doctor from the Recent model
#             calling_profiles = Recent.objects.filter(doctor__in=matching_doctors).values('profile')
#
#             # Extract the profile IDs from the query result
#             profile_ids = calling_profiles.values_list('profile', flat=True)
#
#             # Count the occurrences of each profile ID
#             profile_id_counts = Counter(profile_ids)
#
#             # Retrieve the Profile instances based on the unique profile IDs
#             profiles = Profile.objects.filter(id__in=profile_id_counts.keys())
#
#             # Duplicate phone numbers based on the number of occurrences in the result set
#             profiles_data = [{'phone_number': profile.phone_number, 'nick_name': profile.nick_name,'time':Recent.time} for profile in profiles for _ in range(profile_id_counts[profile.id])]
#
#             # return Response({'profiles': profiles_data}, status=status.HTTP_200_OK)
#             return Response(profiles_data, status=status.HTTP_200_OK)
#
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
class AddRecent(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        doctor_username = request.data.get('doctor_username')
        time=timezone.now()
        try:
            # Get the profile instance based on the phone number
            profile_instance = Profile.objects.get(phone_number=phone)

            # Get the doctor instance based on the username
            doctor_instance = DoctorData.objects.get(username=doctor_username)

            # Create a new Recent instance associating the profile and doctor
            Recent.objects.create(profile=profile_instance, doctor=doctor_instance,time=time)

            return Response({'message': f'Successfully associated {doctor_username} with {phone}'}, status=status.HTTP_201_CREATED)

        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found for the given phone number'}, status=status.HTTP_404_NOT_FOUND)

        except DoctorData.DoesNotExist:
            return Response({'error': 'Doctor not found for the given username'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class AddRecent(APIView):
#     def post(self, request):
#         phone = request.data.get('phone')
#         doctor_username = request.data.get('doctor_username')
#         time = timezone.now()
#         try:
#             # Get the profile instance based on the phone number
#             profile_instance = Profile.objects.get(phone_number=phone)
#
#             # Get the doctor instances based on the username
#             doctor_instances = DoctorData.objects.filter(username=doctor_username)
#
#             # Create a new Recent instance associating the profile and doctors
#             recent_instance = Recent.objects.create(profile=profile_instance, time=time)
#             recent_instance.doctor.set(doctor_instances)
#
#             return Response({'message': f'Successfully associated {doctor_username} with {phone}'}, status=status.HTTP_201_CREATED)
#
#         except Profile.DoesNotExist:
#             return Response({'error': 'Profile not found for the given phone number'}, status=status.HTTP_404_NOT_FOUND)
#
#         except DoctorData.DoesNotExist:
#             return Response({'error': 'Doctor not found for the given username'}, status=status.HTTP_404_NOT_FOUND)
#
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GetRecentDoctors(APIView):
    def get(self, request, phone_number):
        try:
            # Get the profile instance based on the phone number
            profile_instance = Profile.objects.get(phone_number=phone_number)

            # Fetch doctors added under the profile from the Recent model
            added_doctors = Recent.objects.filter(profile=profile_instance)

            # Serialize the recent data
            serializer = RecentSerializer(added_doctors, many=True)

            # return Response({'doctors': serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found for the given phone number'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


from AdminSide.serializers import DoctorDataSerializer


class AddRatingView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        username = request.data.get('username')
        rating_value = request.data.get('rating_value')
        try:
            # Get the profile and doctor objects
            doctor = DoctorData.objects.get(username=username)
            profile = Profile.objects.get(phone_number=phone)

            # Check if a rating already exists for this profile-doctor pair
            rating= Rating.objects.create(doctor=doctor,profile=profile,rating_value=rating_value)

            # If the rating already exists, update the rating_value
            # if not created:
            #     rating.rating_value = rating_value
            rating.save()

            return Response({'message': 'Rating submitted successfully.'}, status=status.HTTP_200_OK)

        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

        except DoctorData.DoesNotExist:
            return Response({'error': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DoctorAverageRatingView(APIView):
    def post(self, request):
        username = request.data.get('username')

        try:
            doctor = DoctorData.objects.get(username=username)
            ratings = Rating.objects.filter(doctor=doctor)

            if not ratings.exists():
                return Response({'average_rating': 0}, status=status.HTTP_200_OK)

            total_ratings = ratings.count()
            sum_ratings = sum(rating.rating_value for rating in ratings)
            average_rating = sum_ratings / total_ratings

            return Response({'average_rating': average_rating}, status=status.HTTP_200_OK)

        except DoctorData.DoesNotExist:
            return Response({'error': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SetUserOnline(APIView):
    def post(self, request):
        phone = request.data.get('phone')

        try:
            # Get the doctor instance
            profile = Profile.objects.get(phone_number=phone)

            # Set is_online to True
            profile.is_online = True
            profile.save()

            # Serialize the doctor data
            serializer = ProfileSerializer(profile)
            serialized_data = serializer.data

            # Include the serialized data in the response
            response_data = {
                'detail': 'User retrieved successfully',
                'User_data': serialized_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except DoctorData.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SetUserOffline(APIView):
    def post(self, request):
        phone = request.data.get('phone')

        try:
            # Get the doctor instance
            profile = Profile.objects.get(phone_number=phone)

            # Set is_online to True
            profile.is_online = False
            profile.save()

            # Serialize the doctor data
            serializer = ProfileSerializer(profile)
            serialized_data = serializer.data

            # Include the serialized data in the response
            response_data = {
                'detail': 'User data',
                'doctor_data': serialized_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except DoctorData.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class OnlineUserListView(APIView):
    def get(self, request):
        try:
            # Filter doctors with is_online=True
            online_user = Profile.objects.filter(is_online=True)

            # Serialize the list of online doctors
            serializer = ProfileSerializer(online_user, many=True)
            serialized_data = serializer.data

            # Include the serialized data in the response
            response_data = {
                'detail': 'Online users',
                'online_user': serialized_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class AverageRatingView(generics.RetrieveAPIView):
#     serializer_class = RatingSerializer
#
#     def get_object(self):
#         doctor_username = self.kwargs['doctor_username']
#         doctor = get_object_or_404(DoctorData, username=doctor_username)
#
#         ratings = Rating.objects.filter(doctor=doctor)
#         total_ratings = ratings.count()
#
#         if total_ratings == 0:
#             return {'averageRating': 0}
#
#         sum_ratings = sum(rating.rating_value for rating in ratings)
#         average_rating = sum_ratings / total_ratings
#
#         return {'averageRating': average_rating}

class ContactUsCreateAPIView(APIView):
    def post(self, request):
        phone_no= request.data.get('phone_no')
        firstname = request.data.get('firstname')
        Lastname = request.data.get('Lastname')
        email = request.data.get('email')
        subject = request.data.get('subject')
        description = request.data.get('description')

        # Check if a profile with the given phone number exists
        try:
            # Assuming you have a serializer for ContactUs
            contact_serializer = ContactSerializer(data={
                'phone_no': phone_no,  # Assuming phone is a ForeignKey in ContactUs
                'firstname': firstname,
                'Lastname': Lastname,
                'email': email,
                'subject': subject,
                'description': description,
            })

            if contact_serializer.is_valid():
                contact_serializer.save()
                return Response({'message': 'Successfully registered your Query'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': contact_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self,request):
        try:
            contact= ContactUs.objects.all()

            # Serialize the data
            serializer = ContactSerializer(contact, many=True)

            # Return the serialized data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserCount(APIView):
    def get(self,request):
        try:
           user=Profile.objects.count()
           return Response({'user': user}, status=status.HTTP_200_OK)
        except Exception as e:
                print(str(e))  # Log the exception for debugging
                return Response({'error': 'Error occurred while fetching user count.'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Create your views here.
class get_user_profile(APIView):
    def post(self, request):
        phone = request.data.get('phone')

        if not phone:
            return Response({'error': 'phone provided.'}, status=status.HTTP_400_BAD_REQUEST)
        # Validate phone number (you may want to replace 'validate_phone' with your own validation logic)

        try:
            profile = Profile.objects.get(phone_number=phone)
            serializer = ProfileSerializer(instance=profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UserDelete(APIView):
    def post(self,request):
        phone = request.data.get('phone')

        if not phone:
            return Response({'error': 'phone provided.'}, status=status.HTTP_400_BAD_REQUEST)
        # Validate phone number (you may want to replace 'validate_phone' with your own validation logic)
        try:
            profile = Profile.objects.get(phone_number=phone)
            profile.delete()
            return Response({'error':'User deleted'},status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



