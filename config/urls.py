from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# ✅ Optional root route for a friendly API landing message
def home(request):
    return JsonResponse({
        "message": "Welcome to the Ticketing API 🚀",
        "endpoints": {
            "accounts": "/api/accounts/",
            "tickets": "/api/tickets/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path('', home, name='api_home'),  # 👈 Base URL now shows this message
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('tickets.urls')),
]
