from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TicketViewSet

router = DefaultRouter()
router.register('tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
]
