from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from tickets.views import RegisterView  # make sure you have a RegisterView for user registration

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Auth endpoints
    path('api/auth/register/', RegisterView.as_view(), name='register'),  # user registration
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # get JWT tokens
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh access token
]
