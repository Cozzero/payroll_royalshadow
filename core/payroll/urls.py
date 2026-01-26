from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payroll.views import PayrollViewSet
from payroll.views import GeneratePayrollView
from payroll.views import home, contact, services


router = DefaultRouter()

router.register(r'payroll', PayrollViewSet, basename='payroll')
urlpatterns = router.urls

urlpatterns = [
    path('core/payroll/services/payroll_services', GeneratePayrollView.as_view(), name='generate-payroll'),
]
