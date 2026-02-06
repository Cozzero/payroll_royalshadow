from rest_framework import serializers
from .models import User, Company

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'company', 'role']
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        models = Company
        fields = ['company name', 'address', 'contact no']

 
