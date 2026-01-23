from django.contrib import admin
from .models import AttendanceRecord

# Register your models here.
@admin.register(AttendanceRecord)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    search_fields = ('employee__username', 'date', 'status')
    list_filter = ('status', 'date')