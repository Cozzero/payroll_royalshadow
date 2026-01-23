from rest_framework.routers import DefaultRouter
from .views import AttendanceRecordViewSet

routers = DefaultRouter()
routers.register(r'attendancerecords', AttendanceRecordViewSet, basename='AttendanceRecord')

urlpatterns = routers.urls
