from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    name = models.CharField(max_length=100)  # Name of the habit
    description = models.TextField(blank=True, null=True)  # Description of the habit
    start_date = models.DateField()  # The date the user starts the habit
    end_date = models.DateField(blank=True, null=True)  # The date the user wants to stop the habit (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the habit was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the habit was last updated


    def get_absolute_url(self):
        return '/'