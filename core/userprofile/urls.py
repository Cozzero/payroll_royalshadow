from rest_framework.routers import DefaultRouter
from userprofile.views import userProfileViewSet
from django.urls import path, include

routers = DefaultRouter()
routers.register(r'userprofile', userProfileViewSet, basename='UserProfile')

#urlpatterns = routers.urls
urlpatterns = routers.urls

# urlpatterns = [
#     path('api/', include('userprofile.urls'))
# ]