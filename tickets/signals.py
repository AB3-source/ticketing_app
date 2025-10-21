from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Ticket

@receiver(post_save, sender=Ticket)
def ticket_created_or_updated(sender, instance, created, **kwargs):
    """Handles notifications when a ticket is created or updated."""
    if created:
        print(f"📩 New ticket created: '{instance.title}' by {instance.created_by.username}")
    else:
        # Detect assignment changes
        old_instance = Ticket.objects.filter(pk=instance.pk).first()
        if old_instance and old_instance.assigned_to != instance.assigned_to:
            assigned_to = instance.assigned_to.username if instance.assigned_to else "Unassigned"
            print(f"👥 Ticket '{instance.title}' reassigned to: {assigned_to}")

        # Detect status change
        if old_instance and old_instance.status != instance.status:
            print(f"🔄 Ticket '{instance.title}' status changed to: {instance.status}")
