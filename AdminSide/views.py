from django.shortcuts import render
from rest_framework import generics,mixins
from AdminSide.models import DoctorData,Languages,Specality
from rest_framework.views import APIView
from AdminSide.serializers import  DoctorDataSerializer,LanguageSerializer,SpecializationSerializer
from rest_framework.response import Response
from rest_framework import status

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


class DoctordatView(generics.ListAPIView):
    queryset = DoctorData.objects.all()
    serializer_class =  DoctorDataSerializer
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        DOB=request.data.get('DOB')
        Dp=request.data.get('Dp')
        Gender=request.data.get('Gender')
        Language=request.data.get('Language', [])
        Specialization=request.data.get('Specialization',[])
        CurrentAddress=request.data.get('CurrentAddress')
        permanentAddress=request.data.get('permanentAddress')
        name=request.data.get('name')
        phone=request.data.get('phone')
        Email=request.data.get('Email')
        Degrees=request.data.get('Degrees')
        Diplomas=request.data.get('Diplomas')
        References=request.data.get('References')
        Certificates=request.data.get('Certificates')
        RCI=request.data.get('RCI')
        PAN=request.data.get('PAN')
        Aadhaar=request.data.get('Aadhaar')
        GST=request.data.get('GST')
        Aboutme=request.data.get('Aboutme')
        Education=request.data.get('Education')
        Experience=request.data.get('Experience')
        callDuration=request.data.get('callDuration')
        try:

            # DoctorData.save()
            doctor = DoctorData.objects.create(
                username=username,
                password=password,
                phone=phone,
                DOB=DOB,
                Dp=Dp,
                Gender=Gender,
                CurrentAddress=CurrentAddress,
                permanentAddress=permanentAddress,
                name=name,
                Email=Email,
                Degrees=Degrees,
                Diplomas=Diplomas,
                References=References,
                Certificates=Certificates,
                RCI=RCI,
                PAN=PAN,
                Aadhaar=Aadhaar,
                GST=GST,
                Aboutme=Aboutme,
                Education=Education,
                Experience=Experience,
                callDuration=callDuration
            )
            doctor.Language.add(*Language)
            doctor.Specialization.add(*Specialization)
            doctor.save()
            return Response({'message': 'Doctor data created successfully.'}, status=status.HTTP_201_CREATED)
        # except IntegrityError:
        #     return Response({'error': 'Duplicate entry. Doctor with the same phone number already exists.'},
        #                     status=status.HTTP_409_CONFLICT)
        except Exception as e:
            print(str(e))  # Log the exception for debugging
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class LanguageView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class LanguageUpdateanddeletView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Languages.objects.all()
    serializer_class = LanguageSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
class SpecializationView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Specality.objects.all()
    serializer_class = SpecializationSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class SpecializationUpdateandDeleteView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Specality.objects.all()
    serializer_class = SpecializationSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)



        # Create your views here.
