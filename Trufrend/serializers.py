from rest_framework import serializers
from Trufrend.models import Otp,Profile,Video,Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Challenge
        fields='__all__'
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_file')