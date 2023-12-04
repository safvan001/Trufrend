from django.shortcuts import render
from rest_framework import generics
from AdminSide.models import DoctorData,Languages,Specality
from rest_framework.views import APIView
from AdminSide.serializers import  DoctorDataSerializer
from rest_framework.response import Response
from rest_framework import status

class DoctorDataView(generics.ListCreateAPIView):
    queryset = DoctorData.objects.all()
    serializer_class =  DoctorDataSerializer


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
