from rest_framework.routers import DefaultRouter
from salary.views import SalaryRecordViewSet

routers = DefaultRouter()
routers.register(r'salaryrecords', SalaryRecordViewSet, basename='SalaryRecord')

urlpatterns = routers.urls