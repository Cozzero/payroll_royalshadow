from rest_framework.routers import DefaultRouter
from .views import PayrollViewSet
# from .generatedpayroll import GeneratePayrollView

routers = DefaultRouter()
routers.register(r'payroll', PayrollViewSet, basename='payroll')
urlpatterns = routers.urls


# urlpatterns = [
#     path('core.generatedpayroll', GeneratePayrollView.as_view(), name='generatedpayroll'),
# ]


