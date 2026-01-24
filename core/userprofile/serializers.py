from rest_framework import serializers
from .models import userProfile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = '__all__'
