from django.shortcuts import render
from rest_framework import viewsets
from .models import salaryRecord
from .serializers import salaryRecordSerializer
class salaryRecordViewSet(viewsets.ModelViewSet):
    queryset = salaryRecord.objects.all()
    serializer_class = salaryRecordSerializer


# Create your views here.
