"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
#     path('api/', include('attendance.urls')),
#     path('api/', include('salary.urls')),
#     path('api/', include('payroll.urls')),
#     path('api/', include('userprofile.urls')),
#     path('api/auth/', include('rest_framework.urls')),
]