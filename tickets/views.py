from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ticket, AuditLog
from .serializers import TicketSerializer
from .permissions import IsTicketOwnerOrReadOnly

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated, IsTicketOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'department', 'category']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'priority', 'status']

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Ticket.objects.filter(is_active=True)
        elif user.role == 'support':
            return Ticket.objects.filter(is_active=True, assigned_to=user)
        return Ticket.objects.filter(is_active=True, created_by=user)

    def perform_create(self, serializer):
        ticket = serializer.save(created_by=self.request.user)
        AuditLog.objects.create(user=self.request.user, action='CREATE', ticket=ticket)

    def perform_update(self, serializer):
        ticket = serializer.save()
        AuditLog.objects.create(user=self.request.user, action='UPDATE', ticket=ticket)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        AuditLog.objects.create(user=self.request.user, action='DELETE', ticket=instance)