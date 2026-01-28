from django.shortcuts import render
from rest_framework import viewsets
from .models import userProfile
from .serializers import userProfileSerializer
class userProfileViewSet(viewsets.ModelViewSet):
    queryset = userProfile.objects.select_related('employee').all()
    serializer_class = userProfileSerializer
