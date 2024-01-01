from rest_framework import serializers
from Doctor.models import Feedback
from Trufrend.serializers import ProfileSerializer
from AdminSide.serializers import DoctorDataSerializer

class FeedbackSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    doctor=DoctorDataSerializer()

    class Meta:
        model=Feedback
        fields='__all__'
