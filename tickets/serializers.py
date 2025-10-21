from rest_framework import serializers
from .models import Ticket, Department, Category, AuditLog

class TicketSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True, allow_null=True)

    class Meta:
        model = Ticket
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    ticket_title = serializers.CharField(source='ticket.title', read_only=True)

    class Meta:
        model = AuditLog
        fields = ['id', 'user_name', 'action', 'ticket_title', 'timestamp']
