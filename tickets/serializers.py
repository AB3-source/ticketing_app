from rest_framework import serializers
from .models import Ticket, Department, Category

class TicketSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True, allow_null=True)

    class Meta:
        model = Ticket
        fields = '__all__'
