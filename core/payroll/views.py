from rest_framework.response import Response
from rest_framework.decorators import action

 

from rest_framework import viewsets

from .models import userProfile, SalaryRecord, AttendanceRecord
from .serializers import UserProfileSerializer, SalaryRecordSerializer, AttendanceRecordSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = userProfile.objects.all()
    serializer_class = UserProfileSerializer
class SalaryRecordViewSet(viewsets.ModelViewSet):
    queryset = SalaryRecord.objects.all()
    serializer_class = SalaryRecordSerializer
class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response

# @APIView(['GET'])
# class test_api(APIView):
#     def test_api(request):
#         return Response({"status": "Payroll API is working!"})
