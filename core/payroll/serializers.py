from rest_framework import serializers
from .models import payroll
class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = payroll
        fields = ['__all__']