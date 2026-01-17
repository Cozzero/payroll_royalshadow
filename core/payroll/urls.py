from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SalaryRecordViewSet, AttendanceRecordViewSet
from .views import test_api
router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')
router.register(r'salaryrecords', SalaryRecordViewSet, basename='salaryrecord')
router.register(r'attendancerecords', AttendanceRecordViewSet, basename='attendancerecord')
urlpatterns = [
    path('', include(router.urls)),
    ]
