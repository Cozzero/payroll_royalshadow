from django.contrib import admin
from .models import payroll

@admin.register(payroll)
class payrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'employee_id', 'amount', 'generated_on', 'month')
    search_fields = ('name', 'employee_id', 'generate_on')
    list_filter = ['month']
