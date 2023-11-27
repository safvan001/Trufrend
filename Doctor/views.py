from django.shortcuts import render
from Doctor.models import Stories
from Doctor.serializers import StoriesSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import generics
from django.utils import timezone
# Create your views here.
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





