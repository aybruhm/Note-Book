from django.db import models
from django.utils import timezone


class Note(models.Model):
    title     = models.CharField(max_length=100)
    content   = models.TextField(max_length=600)
    category  = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title