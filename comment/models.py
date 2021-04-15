from django.db import models
from django.utils import timezone
from author.models import Author
from post.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name="comment",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
        )
    commenter = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=timezone.now)
