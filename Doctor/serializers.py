from rest_framework import serializers
from Doctor.models import Feedback,Schedule
from Trufrend.serializers import ProfileSerializer
from AdminSide.serializers import DoctorDataSerializer

class FeedbackSerializer(serializers.ModelSerializer):
    doctor=DoctorDataSerializer()
    class Meta:
        model=Feedback
        fields='__all__'
class ScheduleSerilaizer(serializers.ModelSerializer):
    user=ProfileSerializer()
    counselor = DoctorDataSerializer()
    class Meta:
        model=Schedule
        fields = '__all__'

