from django.contrib import admin
from .models import userProfile

@admin.register(userProfile)
class userProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'department', 'visa_category', 'passport_no')
    search_fields = ('employee__id', 'name', 'visa_category')
    list_filter = ['passport_no']