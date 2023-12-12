from django.shortcuts import render
from rest_framework import generics,mixins
from AdminSide.models import DoctorData,Stories,Quotes #Languages,Specality
from rest_framework.views import APIView
from AdminSide.serializers import  DoctorDataSerializer,StoriesSerializer,QuotesSerializer #LanguageSerializer,SpecializationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

# class DoctorDataView(generics.ListCreateAPIView):
#     queryset = DoctorData.objects.all()
#     serializer_class =  DoctorDataSerializer


class AddLanguage(APIView):
    def post(self,request):
        try:
            username=request.data.get('username')
            Language_ids = request.data.get('Language_ids', [])

            if not Language_ids:
                return Response({'error': 'Language_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)
            if not username:
                return Response({'error': 'username provided.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = DoctorData.objects.get(username=username)
            except DoctorData.DoesNotExist:
                return Response({'error': 'Username not found.'}, status=status.HTTP_404_NOT_FOUND)

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
            user.Language.add(*valid_languages)

            return Response({'message': 'Language added to the profile successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class AddSpecialization(APIView):
    def post(self,request):
        try:
            username=request.data.get('username')
            specality_ids = request.data.get('specality_ids', [])

            if not specality_ids:
                return Response({'error': 'specality_ids not provided.'}, status=status.HTTP_400_BAD_REQUEST)

            if not username:
                return Response({'error': 'username provided.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = DoctorData.objects.get(username=username)
            except DoctorData.DoesNotExist:
                return Response({'error': 'Username not found.'}, status=status.HTTP_404_NOT_FOUND)

            valid_speciality = []
            for speciality_id in specality_ids:
                try:
                    specality = Specality.objects.get(id=speciality_id)
                    if specality not in valid_speciality:  # Ensure uniqueness
                        valid_speciality.append(specality)
                except Specality.DoesNotExist:
                    return Response({'error': f'Specality with ID {speciality_id} not found.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            # Add the unique challenges to the profile using the many-to-many relationship
            user.Specialization.add(*valid_speciality)

            return Response({'message': 'Specialzation added to the profile successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.db import IntegrityError


class DoctordatView(generics.ListCreateAPIView):
    queryset = DoctorData.objects.all()
    serializer_class =  DoctorDataSerializer
    # def post(self,request):
    #     username=request.data.get('username')
    #     password=request.data.get('password')
    #     DOB=request.data.get('DOB')
    #     Dp=request.data.get('Dp')
    #     Gender=request.data.get('Gender')
    #     # Language=request.data.get('Language', [])
    #     # Specialization=request.data.get('Specialization',[])
    #     CurrentAddress=request.data.get('CurrentAddress')
    #     permanentAddress=request.data.get('permanentAddress')
    #     name=request.data.get('name')
    #     phone=request.data.get('phone')
    #     Email=request.data.get('Email')
    #     Degrees=request.data.get('Degrees')
    #     Diplomas=request.data.get('Diplomas')
    #     References=request.data.get('References')
    #     Certificates=request.data.get('Certificates')
    #     RCI=request.data.get('RCI')
    #     PAN=request.data.get('PAN')
    #     Aadhaar=request.data.get('Aadhaar')
    #     GST=request.data.get('GST')
    #     Aboutme=request.data.get('Aboutme')
    #     Education=request.data.get('Education')
    #     Experience=request.data.get('Experience')
    #     callDuration=request.data.get('callDuration')
    #     try:
    #
    #         # DoctorData.save()
    #         doctor = DoctorData.objects.create(
    #             username=username,
    #             password=password,
    #             phone=phone,
    #             DOB=DOB,
    #             Dp=Dp,
    #             Gender=Gender,
    #             CurrentAddress=CurrentAddress,
    #             permanentAddress=permanentAddress,
    #             name=name,
    #             Email=Email,
    #             Degrees=Degrees,
    #             Diplomas=Diplomas,
    #             References=References,
    #             Certificates=Certificates,
    #             RCI=RCI,
    #             PAN=PAN,
    #             Aadhaar=Aadhaar,
    #             GST=GST,
    #             Aboutme=Aboutme,
    #             Education=Education,
    #             Experience=Experience,
    #             callDuration=callDuration
    #         )
    #         # doctor.Language.add(*Language)
    #         # doctor.Specialization.add(*Specialization)
    #         doctor.save()
    #         return Response({'message': 'Doctor data created successfully.'}, status=status.HTTP_201_CREATED)
    #     # except IntegrityError:
    #     #     return Response({'error': 'Duplicate entry. Doctor with the same phone number already exists.'},
    #     #                     status=status.HTTP_409_CONFLICT)
    #     except Exception as e:
    #         print(str(e))  # Log the exception for debugging
    #         return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DoctorUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorData.objects.all()
    serializer_class = DoctorDataSerializer
    lookup_field = 'username'

class StoryView(generics.ListCreateAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer

    def get(self, request, *args, **kwargs):
        # Get the current time
        current_time = timezone.now()

        # Iterate over all Stories instances
        for story in Stories.objects.all():
            # Access the created_at attribute
            created_at = story.created_at

            # Define the threshold (e.g., 2 minutes)
            threshold = timezone.timedelta(days=1)

            # Check if the story is older than the threshold
            if current_time > created_at + threshold:
                # Delete the story if it's older than the threshold
                story.story_file.delete()
                story.delete()

        return self.list(request, *args, **kwargs)

# class StoryCreateView(APIView):
#     def post(self, request):
#
#         username = request.data.get('username')
#         story = request.data.get('story')
#         media_type=request.data.get('media_type')
#
#         try:
#             doctor = DoctorData.objects.get(username=username)
#             sto=Stories.objects.create(doctor=doctor, story_file=story, media_type=media_type)
#
#             serializer = StoriesSerializer(sto)
#             serialized_data = serializer.data
#
#             # Include the serialized data in the response
#             response_data = {
#                 'detail': 'Story added successful',
#                 'story': serialized_data,
#             }
#             return Response(response_data, status=status.HTTP_200_OK)
#             # doctor.save()
#             # return Response({'detail': 'Story created successfully.'}, status=status.HTTP_201_CREATED)
#         except DoctorData.DoesNotExist:
#             return Response({'detail': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#
#     # def get(self, request, *args, **kwargs):
#     #     # Call the list method to return the list of stories
#     #     return self.list(request, *args, **kwargs)
#
#     def delete_old_stories(self):
#         # Get the current time
#         current_time = timezone.now()
#
#         # Iterate over all Stories instances
#         for story in Stories.objects.all():
#             # Access the created_at attribute
#             created_at = story.created_at
#
#             # Define the threshold (e.g., 2 minutes)
#             threshold = timezone.timedelta(minutes=3)
#
#             # Check if the story is older than the threshold
#             if current_time > created_at + threshold:
#                 # Delete the story if it's older than the threshold
#                 story.story_file.delete()
#                 story.delete()
#
#     def list(self, request, *args, **kwargs):
#         # Delete old stories
#         self.delete_old_stories()
#
#         # Return the list of stories
#         queryset = Stories.objects.all()
#         serializer = StoriesSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
class StoryCreateView(APIView):
    def post(self, request):
        username = request.data.get('username')
        story = request.data.get('story')
        media_type = request.data.get('media_type')

        try:
            doctor = DoctorData.objects.get(username=username)
            sto = Stories.objects.create(doctor=doctor, story_file=story, media_type=media_type)

            serializer = StoriesSerializer(sto)
            serialized_data = serializer.data

            # Include the serialized data in the response
            response_data = {
                'detail': 'Story added successfully',
                'story': serialized_data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except DoctorData.DoesNotExist:
            return Response({'detail': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def delete_old_stories(self):
    #     # Get the current time
    #     current_time = timezone.now()
    #
    #     # Iterate over all Stories instances
    #     for story in Stories.objects.all():
    #         # Access the created_at attribute
    #         created_at = story.created_at
    #
    #         # Define the threshold (e.g., 2 minutes)
    #         threshold = timezone.timedelta(minutes=3)
    #
    #         # Check if the story is older than the threshold
    #         if current_time > created_at + threshold:
    #             # Delete the story if it's older than the threshold
    #             story.story_file.delete()
    #             story.delete()
    #
    # def list(self, request, *args, **kwargs):
    #     # Delete old stories
    #     self.delete_old_stories()
    #
    #     # Return the list of stories
    #     queryset = Stories.objects.all()
    #     serializer = StoriesSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

class StoryRetrieveView(APIView):
    def post(self, request):
        username = "safvan"
        try:
            doctor = DoctorData.objects.get(username=username)
            stories = Stories.objects.filter(doctor=doctor)

            serializer = StoriesSerializer(stories, many=True)
            serialized_data = serializer.data

            response_data = {
                'detail': 'Stories retrieved successfully',
                'stories': serialized_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except DoctorData.DoesNotExist:
            return Response({'detail': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Stories.DoesNotExist:
            return Response({'detail': 'No stories found for the given doctor.'}, status=status.HTTP_404_NOT_FOUND)

from django.http import JsonResponse
from django.core.serializers import serialize
from rest_framework import viewsets
import json

from django.http import JsonResponse

from django.http import JsonResponse

def get_all_stories(request):
    # Assuming you have a Stories model
    stories = Stories.objects.all()

    # Serialize the stories using the StoriesSerializer
    serialized_stories = StoriesSerializer(stories, many=True).data

    # Organize stories by doctor username
    doctor_stories = []

    for serialized_story in serialized_stories:
        doctor_data = serialized_story['doctor']

        # Check if the doctor is already in the list
        existing_doctor = next((doc for doc in doctor_stories if doc['doctor_details']['username'] == doctor_data['username']), None)

        if existing_doctor:
            # Add the story to the existing doctor's list
            story = {
                'story_file': serialized_story['story_file'],
                'created_at': serialized_story['created_at'],
                'media_type': serialized_story['media_type']
            }
            existing_doctor['stories'].append(story)
        else:
            # Create a new doctor entry with details and story
            doctor_story = {
                'doctor_details': doctor_data,  # Store doctor details
                'stories': [
                    {
                        'story_file': serialized_story['story_file'],
                        'created_at': serialized_story['created_at'],
                        'media_type': serialized_story['media_type']
                    }
                ]
            }
            doctor_stories.append(doctor_story)

    # Wrap the list in a dictionary with the "doctors" key
    response_data = {'doctors': doctor_stories}

    return JsonResponse(response_data, safe=False)












# class StoryGetView(APIView):
#     def post(self,request):
#         username=request.data.get('username')
#         story=Stories.objects.filter()
#         try:
#             doctor = Stories.doctor.object.get(username=username)
#             story=Stories.objects.filter(doctor=doctor)
#             serializer = StoriesSerializer(story)
#             serialized_data = serializer.data
#
#         # Include the serialized data in the response
#             response_data = {
#                 'story': serialized_data,
#             }
#             return Response(response_data, status=status.HTTP_200_OK)
#         except DoctorData.DoesNotExist:
#             return Response({'detail': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)


class QuotesPostingView(APIView):
    def post(self,request):
        quotes=request.data.get('quotes')
        author=request.data.get('author')
        try:
            quote=Quotes.objects.create(quotes=quotes,author=author)
            serializer=QuotesSerializer(quote)
            serialized_data=serializer.data
            response_data = {
                'detail': 'Quotes added successful',
                'story': serialized_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except DoctorData.DoesNotExist:
            return Response({'detail': 'Unable to found instance of Quotes .'}, status=status.HTTP_404_NOT_FOUND)
    def get(self,request):
        try:
            quote=Quotes.objects.all()
            serializer = QuotesSerializer(quote, many=True)

            # Return the serialized data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class LanguageView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Languages.objects.all()
#     serializer_class = LanguageSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
# class LanguageUpdateanddeletView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Languages.objects.all()
#     serializer_class = LanguageSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
# class SpecializationView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Specality.objects.all()
#     serializer_class = SpecializationSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
# class SpecializationUpdateandDeleteView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Specality.objects.all()
#     serializer_class = SpecializationSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)



        # Create your views here.
