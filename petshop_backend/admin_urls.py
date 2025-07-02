from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserManagementViewSet

router = DefaultRouter()
router.register(r'users', UserManagementViewSet, basename='user-management')
urlpatterns = [
    path('', include(router.urls)),
]

