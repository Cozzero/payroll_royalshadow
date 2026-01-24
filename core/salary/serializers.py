from rest_framework import serializers
from .models import SalaryRecord
class SalaryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryRecord
        fields = '__all__'
