from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class TrackerUser(AbstractUser):
    # refer to ticket model once it has been created
    # current_tickets = models.ManyToManyField()
    display_name = models.CharField(max_length=50)
