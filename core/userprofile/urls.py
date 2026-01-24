from rest_framework.routers import DefaultRouter
from userprofile.views import userProfileViewSet

routers = DefaultRouter()
routers.register(r'userprofiles', userProfileViewSet, basename='UserProfile')

urlpatterns = routers.urls