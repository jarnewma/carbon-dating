from django.shortcuts import render
from author.models import Author
from post.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def author_profile(request, user_id):
    user_obj = Author.objects.get(id=user_id)

    return render(request, "author_detail.html", {
        "author_info": user_obj
    })


@login_required
def home_view(request):
    posts = Post.objects.all()[:10]
    context = {
        "posts": posts
    }
    return render(request, 'home.html', context)


@login_required
def explore_view(request):
    users = Author.objects.filter(id=2)
    matches = Author.objects.all()
    context = {
        "users": users,
        "matches": matches
    }
    return render(request, "explore.html", context)
