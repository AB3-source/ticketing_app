from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ticketing System API",
        default_version='v1',
        description="Comprehensive API documentation for the Ticketing System",
        contact=openapi.Contact(email="support@ticketingapp.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # App routes
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('tickets.urls')),

    # Swagger & Redoc Docs
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
