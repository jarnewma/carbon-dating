from django.db import models
from CustomUser1.models import CustomUser1

# Create your models here.
# Message Model:
#     Sender - ForeignKey(CustomUser)
#     Receiver - ForeignKey(CustomUser)
#     Viewed - BooleanField(default=False)
#     Content - TextField


class Messages(models.Model):
    Sender = models.ForeignKey(
        CustomUser1,
        related_name="Sender",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )
    Receiver = models.ForeignKey(
        CustomUser1,
        related_name="Receiver",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )
    Viewed = models.BooleanField(default=False),
    Content = models.TextField()
