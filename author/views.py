from django.shortcuts import render
from post.models import Post
from author.models import Author
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home_view(request):
    posts = Post.objects.all()[:10]
    context = {
        "posts": posts
    }
    return render(request, 'home.html', context)


def explore_view(request):
    users = Author.objects.filter(id=2)
    matches = Author.objects.all()
    context = {
        "users": users,
        "matches": matches
    }
    return render(request, "explore.html", context)
