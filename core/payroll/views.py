from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from services.payroll_services import generate_salary
from django.contrib.auth.models import User
from .models import payroll
from .serializers import PayrollSerializer
from salary.models import salaryRecord

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = payroll.objects.select_related('employee').all()
    serializer_class = PayrollSerializer

class GeneratePayrollView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = User.objects.get(id=request.data.get('employee_id'))
        present_days, net_salary = generate_salary(
            request.data.get('user'),
            request.data.get('year'),
            request.data.get('month'),

        )
        salaryRecord.objects.create(
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
    


