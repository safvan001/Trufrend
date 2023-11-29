from rest_framework import serializers
from AdminPanel.models import Upload,DoctorDetail,Specialty

class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorDetail
        fields = '__all__'
class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upload
        fields='__all__'












