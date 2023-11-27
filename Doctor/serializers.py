from rest_framework import serializers
from Doctor.models import Stories

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = '__all__'