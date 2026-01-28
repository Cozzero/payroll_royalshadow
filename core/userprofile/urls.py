from rest_framework.routers import DefaultRouter
from userprofile.views import userProfileViewSet

routers = DefaultRouter()
routers.register(r'userprofile', userProfileViewSet, basename='userProfile')

urlpatterns = routers.urls
