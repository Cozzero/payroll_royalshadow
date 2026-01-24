from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payroll.views import PayrollViewSet
from payroll.views import GeneratePayrollView
from payroll.views import home, contact, services

urlpatterns = [
    path('api/', include('payroll.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
]


router = DefaultRouter()
#router.register(r'userprofiles', UserProfileViewSet, basename='userProfile')
#router.register(r'salaryrecords', SalaryRecordViewSet, basename='SalaryRecord')
#router.register(r'attendancerecords', AttendanceRecordViewSet, basename='AttendanceRecord')
router.register(r'payroll', PayrollViewSet, basename='payroll')
urlpatterns = [
    path('', include(router.urls)),
    path('core/payroll/services/payroll_services', GeneratePayrollView.as_view(), name='generate-payroll'),
]
