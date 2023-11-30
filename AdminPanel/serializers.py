from rest_framework import serializers
from django.contrib.auth.models import User
from AdminPanel.models import Upload,DoctorDetail,Specialty,Language


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model=Language
        fields='__all__'
class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class DoctorDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # specialties = SpecialtySerializer(many=True)
    # language = LanguageSerializer(many=True)

    class Meta:
        model = DoctorDetail
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
    #     specialties_data = validated_data.pop('specialties', [])
    #     languages_data=validated_data.pop('language',[])
    #
        user = User.objects.create(**user_data)
        doctor_detail = DoctorDetail.objects.create(user=user, **validated_data)
    #
    #     # Add specialties to the doctor_detail instance using the set() method
    #     doctor_detail.specialties.set(specialties_data)
    #     doctor_detail.language.set(languages_data)

        return doctor_detail
class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upload
        fields='__all__'












