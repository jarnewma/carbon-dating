from django.db import models
from author.models import Author


class NewAdmirer(models.Model):
    admirer = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="new_admirer")
    admiring = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="new_admiring")
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.admiring} is admiring {self.admirer}"
    
