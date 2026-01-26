from rest_framework import serializers
from .models import salaryRecord
class salaryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = salaryRecord
        fields = '__all__'
