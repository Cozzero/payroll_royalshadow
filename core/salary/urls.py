from rest_framework.routers import DefaultRouter
from salary.views import salaryRecordViewSet

routers = DefaultRouter()
routers.register(r'salaryRecord', salaryRecordViewSet, basename='salaryRecord')

urlpatterns = routers.urls