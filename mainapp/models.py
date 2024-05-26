# mainapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date}"
