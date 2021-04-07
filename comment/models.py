from django.db import models
from django.utils import timezone
from author.models import Author
from post.models import Post


class Comment(models.Model):
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=timezone.now)
