from django.db import models
from author.models import Author
from django.utils import timezone


class Message(models.Model):
    sender = models.ForeignKey(
        Author,
        related_name="sender",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )
    receiver = models.ForeignKey(
        Author,
        related_name="receiver",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )
    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField()
