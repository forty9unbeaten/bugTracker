from django.db import models
from django.utils import timezone
from bugTracker_users.models import TrackerUser

# Create your models here.


class BugTicket(models.Model):
    title = models.CharField(max_length=75)
    file_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=500)
    creator = models.ForeignKey(
        TrackerUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='ticket_creator'
    )
    status = models.CharField(
        max_length=11,
        choices=[
            ('open', 'Open'),
            ('in progress', 'In progress'),
            ('complete', 'Complete'),
            ('invalid', 'Invalid')
        ],
        default='open'
    )
    assigned_to = models.ForeignKey(
        TrackerUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ticket_worker'
    )
    completed_by = models.ForeignKey(
        TrackerUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ticket_completer'
    )
    is_invalid = models.BooleanField(default=False)

    def __str__(self):
        return self.title
