from django.db import models
from author.models import Author


class NewAdmirer(models.Model):
    admirer = models.ForeignKey(Author, on_delete=models.CASCADE)
    admiring = models.ForeignKey(Author, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
