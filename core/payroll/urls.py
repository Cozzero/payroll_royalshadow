from rest_framework.routers import DefaultRouter
from payroll.views import PayrollViewSet
# from .generatedpayroll import GeneratePayrollView


router = DefaultRouter()
router.register(r'payroll', PayrollViewSet, basename='payroll')
urlpatterns = router.urls


# urlpatterns = [
#     path('core.generatedpayroll', GeneratePayrollView.as_view(), name='generatedpayroll'),
# ]


