from django.db import models
from django.utils import timezone
from author.models import Author


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    caption = models.CharField(max_length=140)
    image = models.ImageField(
        upload_to="images/",
        height_field=None,
        width_field=None,
        max_length=None
        )
    timestamp = models.DateTimeField(default=timezone.now)
