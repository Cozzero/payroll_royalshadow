from django.contrib import admin
from .models import userProfile, SalaryRecord, AttendanceRecord, payroll
admin.site.register(userProfile)
admin.site.register(SalaryRecord)
admin.site.register(AttendanceRecord)
admin.site.register(payroll)