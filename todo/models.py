# todo/models.py
from django.db import models
from accounts.models import NormalUser

class Todo(models.Model):
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
