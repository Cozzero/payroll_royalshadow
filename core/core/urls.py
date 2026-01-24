"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('payroll.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('', include('attendance.urls')),
    path('', include('payroll.urls')),
    path('', include('userprofile.urls')),
    path('', include('salary.urls')),
    path('api/auth/', include('rest_framework.urls')),
    # path('api/', include('payroll.urls')),
    # path('api/attendance/', include('attendance.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('', include('payroll.urls')),
    #path('api/auth/', include('rest_framework.urls')),
    
]

