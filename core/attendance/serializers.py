from rest_framework import serializers
from .models import AttendanceRecord

class AttendanceRecordSerializer(serializers.ModelSerializer):
    employee_name = serializers.ReadOnlyField(source='employee.username', read_only=True)
    class Meta:
        model = AttendanceRecord
        fields = ['id', 'employee', 'employee_name', 'status', 'date']
