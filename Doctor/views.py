from django.shortcuts import render
from Doctor.models import Stories
from Doctor.serializers import StoriesSerializer
from AdminSide.serializers import  DoctorDataSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import generics
from django.utils import timezone
from rest_framework.views import APIView
from AdminSide.models import DoctorData
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
class DoctorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorData.objects.all()
    serializer_class = DoctorDataSerializer
    lookup_field = 'username'  # Use 'username' as the lookup field

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Doctor data updated successfully.'})

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Doctor data deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
class storiesView(generics.ListCreateAPIView):
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
            threshold = timezone.timedelta(minutes=3)

            # Check if the story is older than the threshold
            if current_time > created_at + threshold:
                # Delete the story if it's older than the threshold
                story.story_file.delete()
                story.delete()

        return self.list(request, *args, **kwargs)





