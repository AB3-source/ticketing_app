from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import TicketAccessPermission  # updated permission class


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated, TicketAccessPermission]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'department', 'category']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'priority', 'status']

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            # Admins see all active tickets
            return Ticket.objects.filter(is_active=True)

        elif user.role == 'support':
            # Support sees assigned tickets
            return Ticket.objects.filter(is_active=True, assigned_to=user)

        # Regular users see only their own tickets
        return Ticket.objects.filter(is_active=True, created_by=user)

    def perform_create(self, serializer):
        """Attach the creator to each new ticket automatically."""
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        """Soft delete instead of hard delete."""
        instance.is_active = False
        instance.save()

    def update(self, request, *args, **kwargs):
        """
        Allow only admins/support to update ticket status or assignment.
        Regular users cannot update tickets once created.
        """
        user = request.user
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Allow Admins or Support assigned to this ticket
        if user.role not in ['admin', 'support']:
            return Response({'detail': 'You do not have permission to modify this ticket.'},
                            status=status.HTTP_403_FORBIDDEN)

        # Support can only update their assigned tickets
        if user.role == 'support' and instance.assigned_to != user:
            return Response({'detail': 'You can only update tickets assigned to you.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
