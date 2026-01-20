from rest_framework import serializers
from payroll.models import userProfile, SalaryRecord, AttendanceRecord, payroll

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = ['user', 'name', 'employee_id', 'phone_number', 'passport_number', 'visa_type']

class SalaryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryRecord
        fields = ['user', 'name', 'employee_id', 'basic_salary', 'allowances', 'deductions', 'net_salary', 'pay_date']

class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ['user', 'name', 'employee_id', 'date', 'check_in', 'check_out']

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = payroll
        fields = ['user', 'name', 'employee_id', 'month', 'total_present_days', 'net_salary', 'generated_on']
        


        