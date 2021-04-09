from django.shortcuts import render
from post.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home_view(request):
    posts = Post.objects.all()[:10]
    context = {
        "posts": posts
    }
    return render(request, 'home.html', context)
