from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SalaryRecordViewSet, AttendanceRecordViewSet, PayrollViewSet
from payroll.views import GeneratePayrollView

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userProfile')
router.register(r'salaryrecords', SalaryRecordViewSet, basename='SalaryRecord')
router.register(r'attendancerecords', AttendanceRecordViewSet, basename='AttendanceRecord')
router.register(r'payroll', PayrollViewSet, basename='payroll')
urlpatterns = [
    path('', include(router.urls)),
    path('core/payroll/services/payroll_services', GeneratePayrollView.as_view(), name='generate-payroll'),
]
