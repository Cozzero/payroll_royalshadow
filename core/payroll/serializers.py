from rest_framework import serializers
from payroll.models import userProfile, SalaryRecord, AttendanceRecord, payroll


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = '__all__'


class SalaryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryRecord
        fields = '__all__'
class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'
class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = payroll
        fields = '__all__'


        