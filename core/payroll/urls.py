from django.urls import path
from rest_framework.routers import DefaultRouter
from payroll.views import PayrollViewSet
from .generatedpayroll import GeneratePayrollView


router = DefaultRouter()
router.register(r'payroll', PayrollViewSet, basename='payroll')


urlpatterns = [
    path('core/services/payroll_services', GeneratePayrollView.as_view(), name='generatedpayroll'),
]

urlpatterns = router.urls