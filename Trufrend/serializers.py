from rest_framework import serializers
from Trufrend.models import Profile,Video,Challenge,VideoPack,Favorite


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    # challenges=ChallengeSerializer(many=True)
    class Meta:
        model = Profile
        fields = '__all__'




    # def update(self, instance, validated_data):
    #     challenges_data = validated_data.pop('challenges', None)  # Use None as default
    #
    #     instance = super().update(instance, validated_data)
    #
    #     if challenges_data is not None:
    #         instance.challenges.set(challenges_data)
    #
    #     return instance
class DpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields= ('dp',)


class VideoPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPack
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    video_files=VideoPackSerializer(many=True)
    class Meta:
        model = Video
        fields = '__all__'
class FavoriteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'









