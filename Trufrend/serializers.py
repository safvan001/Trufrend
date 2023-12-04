from rest_framework import serializers
from Trufrend.models import Profile,Video,Challenge,VideoPack,Favorite,ContactUs


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'
class VideoPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPack
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    video_files=VideoPackSerializer(many=True)
    class Meta:
        model = Video
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    challenges=ChallengeSerializer(many=True)
    videoFavour = VideoSerializer(many=True)
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



class FavoriteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model =ContactUs
        fields ='__all__'


    # def create(self, validated_data):
    #     Favour_data = validated_data.pop('Favour_data',[])
    #     video=VideoFavourite.videoFavour.set(Favour_data)
    #     return video
# class StorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Stories
#         fields ='__all__'









