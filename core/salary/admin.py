from django.contrib import admin
from .models import salaryRecord

@admin.register(salaryRecord)
class salaryRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'amount', 'date')
    search_fields = ('user', 'employee_id')
    list_filter = ['date']
