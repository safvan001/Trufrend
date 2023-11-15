from rest_framework import serializers
from Trufrend.models import Profile,Video,Challenge,VideoPack


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    # challenges=ChallengeSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('dp','name','nick_name','challenges')

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
# class VideoPackSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = VideoPack
#         fields = ('title',)
#
# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = ('id','title','description','video_file')
class VideoPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPack
        fields = ('title',)

class VideoSerializer(serializers.ModelSerializer):
    # title=VideoPackSerializer()
    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_file')


