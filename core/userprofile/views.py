from django.shortcuts import render
from rest_framework import viewsets
from .models import userProfile
from .serializers import UserProfileSerializer
class userProfileViewSet(viewsets.ModelViewSet):
    queryset = userProfile.objects.all()
    serializer_class = UserProfileSerializer


# Create your views here.
