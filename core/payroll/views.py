from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status

from .models import userProfile, SalaryRecord, AttendanceRecord, payroll
from .serializers import UserProfileSerializer, SalaryRecordSerializer, AttendanceRecordSerializer, PayrollSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = userProfile.objects.all()
    serializer_class = UserProfileSerializer
class SalaryRecordViewSet(viewsets.ModelViewSet):
    queryset = SalaryRecord.objects.all()
    serializer_class = SalaryRecordSerializer
class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
class PayrollViewSet(viewsets.ModelViewSet):
    queryset = payroll.objects.all()
    serializer_class = PayrollSerializer
