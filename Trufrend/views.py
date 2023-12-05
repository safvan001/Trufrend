from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from twilio.rest import Client

from Trufrend.models import Profile,Video,Challenge,VideoPack,Favorite,ContactUs
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
from Trufrend.serializers import ProfileSerializer,VideoSerializer,VideoPackSerializer,ChallengeSerializer,DpSerializer,FavoriteProfileSerializer,ContactSerializer
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
        phone = "+91" + request.data.get('phone')
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


class UserUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class Dp(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = DpSerializer



class Nickname(APIView):
    def post(self, request):
        nick_name = request.data.get('nick_name')
        phone = "+91" + request.data.get('phone')
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
            phone = "+91" + request.data.get('phone')  # Change 'id' to 'profile_id'
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
        phone = "+91"+request.data.get('phone')
        nick_name = request.data.get('nick_name')
        name = request.data.get('name')
        dp=request.data.get('dp')
        challenges=request.data.get('challenges',[])
        videoFavour=request.data.get('videoFavour',[])

        try:
            profile = Profile.objects.get(phone_number=phone)
            profile.nick_name = nick_name
            profile.name = name
            profile.challenges.add(*challenges)
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



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoPackView(generics.ListCreateAPIView):
    queryset = VideoPack.objects.all()
    serializer_class = VideoPackSerializer

class AddToFavoriteView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteProfileSerializer


class RemoveFromFavoriteView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteProfileSerializer

class AddVideoFavouriteView(APIView):
    def post(self,request):
        try:
            phone = "+91" + request.data.get('phone')  # Change 'id' to 'profile_id'
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
            phone = "+91" + request.data.get('phone')  # Change 'id' to 'profile_id'
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




# class VideoFavouriteView(generics.ListCreateAPIView):
#     queryset = VideoFavourite.objects.all()
#     serializer_class=VideoFavouriteSerializer

# class StoriesView(generics.ListCreateAPIView):
#     queryset=Stories.objects.all()
#     serializer_class = StorySerializer

# class ContactusView(APIView):
#     def post(self,request):
#         phone="+91" + request.data.get('phone')
#         firstname=request.data.get('firstname')
#         Lastname=request.data.get('Lastname')
#         email=request.data.get('email')
#         subject=request.data.get('subject')
#         description=request.data.get('description')
#         profile = Profile.objects.get(phone_number=phone)
#         if profile:
#             # Assuming you have a serializer for ContactUs
#             contact_serializer = ContactSerializer(data={
#                 'firstname': firstname,
#                 'Lastname': Lastname,
#                 'email': email,
#                 'subject': subject,
#                 'description': description,
#             })
#             if contact_serializer.is_valid():
#                 contact_serializer.save()
#                 return Response({'message': 'Successfully registered your Query'}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': contact_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#
#         else:
#             return Response({'error': 'Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)


class ContactUsCreateAPIView(APIView):
    def post(self, request):
        phone_no= "+91" + request.data.get('phone_no')
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
        phone = "+91" + request.data.get('phone')

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