import django_filters
from .models import Ticket

class TicketFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Ticket
        fields = {
            'status': ['exact'],
            'priority': ['exact'],
            'department': ['exact'],
            'category': ['exact'],
            'created_by': ['exact'],
            'assigned_to': ['exact'],
        }
