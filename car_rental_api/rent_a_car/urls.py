from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"rentcar", views.RentACarViewSerializer, basename='rentcar'),
router.register(r"vehicle", views.ViewCarSerializer, basename='vehicle'),
router.register(r"new_user", views.NewUserSerializer, basename='new_user')
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls