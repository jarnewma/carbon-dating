from django.db import models
from customuser.models import CustomUser


class NewAdmirer(models.Model):
    admirer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    admiring = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
