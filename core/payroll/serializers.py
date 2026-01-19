from rest_framework import serializers
from payroll.models import userProfile, SalaryRecord, AttendanceRecord

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = ['id', 'user', 'address', 'phone_number', 'passport_number', 'department']

class SalaryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryRecord
        fields = ['id', 'user', 'basic_salary', 'allowances', 'deductions', 'net_salary', 'pay_date']
class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ['id', 'user', 'date', 'check_in', 'check_out']

        