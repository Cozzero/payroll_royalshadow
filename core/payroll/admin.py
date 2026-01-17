from django.contrib import admin
from .models import userProfile, SalaryRecord, AttendanceRecord
admin.site.register(userProfile)
admin.site.register(SalaryRecord)
admin.site.register(AttendanceRecord)