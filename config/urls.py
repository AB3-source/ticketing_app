from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from tickets.views import RegisterView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Auth
    path('api/tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tokens/logout/', LogoutView.as_view(), name='token_logout'),

    # User Registration
    path('api/register/', RegisterView.as_view(), name='register'),

    # Ticket Endpoints
path('api/', include('tickets.urls')),
]
