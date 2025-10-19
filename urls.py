from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    # existing paths...
    path('api/tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tokens/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/tickets/', include('tickets.urls')),
]
