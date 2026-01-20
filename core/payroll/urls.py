from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SalaryRecordViewSet, AttendanceRecordViewSet, PayrollViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')
router.register(r'salaryrecords', SalaryRecordViewSet, basename='SalaryRecord')
router.register(r'attendancerecords', AttendanceRecordViewSet, basename='AttendanceRecord')
router.register(r'payroll', PayrollViewSet, basename='payroll')
urlpatterns = [
    path('', include(router.urls)),
]