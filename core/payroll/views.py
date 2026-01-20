from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from payroll.services.payroll_services import generate_salary
from payroll.models import SalaryRecord
from django.contrib.auth.models import User
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

class GeneratePayrollView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = User.objects.get(id=request.data.get('user_id'))
        present_days, net_salary = generate_salary(
            user,
            request.data.get('year'),
            request.data.get('month')
        )
        SalaryRecord.objects.create(
            user=user, 
            month=f"{request.data.get('year')}-{request.data.get('month')}-01",
            present_days=present_days,
            net_salary=net_salary
        )
        return Response({
            "employee_id": user.userprofile.employee_id,
            "present_days": present_days,
            "net_salary": str(net_salary),
            "message": "Payroll generated successfully."
        }
        )
    