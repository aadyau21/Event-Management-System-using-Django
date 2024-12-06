from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Organizer', 'Organizer'),
        ('Attendee', 'Attendee'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organized_events')
    attendees = models.ManyToManyField(CustomUser, related_name='registered_events')

    def __str__(self):
        return self.title
