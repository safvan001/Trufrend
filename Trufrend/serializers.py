from rest_framework import serializers
from Trufrend.models import Profile,Video,Challenge,VideoPack


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Challenge
        fields='__all__'
class ProfileSerializer(serializers.ModelSerializer):
    # challenges=ChallengeSerializer()
    class Meta:
        model = Profile
        fields = '__all__'
class DpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('dp',)
class VideoPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPack
        fields = ('title',)

class VideoSerializer(serializers.ModelSerializer):
    title=VideoPackSerializer()
    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_file')
