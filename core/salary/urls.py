from rest_framework.routers import DefaultRouter
from salary.views import salaryRecordViewSet

routers = DefaultRouter()
routers.register(r'salaryrecords', salaryRecordViewSet, basename='SalaryRecord')

urlpatterns = routers.urls