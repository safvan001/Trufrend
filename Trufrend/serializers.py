from rest_framework import serializers
from Trufrend.models import Profile,Video,Challenge,VideoPack,Favorite,ContactUs,Rating,Usercount,Languages,Recent



class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'
class LanguageSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Languages
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
    # challenges=ChallengeSerializer(many=True)
    videoFavour = VideoSerializer(many=True)
    from AdminSide.serializers import DoctorDataSerializer
    doctorFavour=DoctorDataSerializer(many=True)
    language=LanguageSerilaizer(many=True)
    # from AdminSide.serializers import DoctorDataSerializer
    # recent_calls=DoctorDataSerializer(many=True)
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
class OnlineUserCountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usercount
        fields='__all__'
class RatingSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(many=True)
    # doctor=DoctorDataSerializer()
    class Meta:
        model = Rating
        fields = '__all__'
class RecentSerializer(serializers.ModelSerializer):
    from AdminSide.serializers import DoctorDataSerializer
    doctor=DoctorDataSerializer()
    # profile = ProfileSerializer()

    class Meta:
        model =Recent
        # exclude = ['profile']
        fields=['id','doctor','time']

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









