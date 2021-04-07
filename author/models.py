from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.utils import timezone
# Create your models here.


class Author(AbstractUser):
    ROCK_CHOICES = (
        ('IGNEOUS', 'Igneous'),
        ('SEDIMENTARY', 'Sedimentary'),
        ('METAMORPHIC', 'Metamorphic')
    )
    rock_type = models.CharField(
        max_length=50, choices=ROCK_CHOICES, null=True)
    interested_in = MultiSelectField(
        max_length=35,
        choices=ROCK_CHOICES,
        null=True
    )
    admirers = models.ManyToManyField(
        'self', symmetrical=False, blank=True, related_name='admiring')
    bio = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    birthday = models.DateField(null=True)
    profilepic = models.ImageField(
        upload_to='users/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.username
