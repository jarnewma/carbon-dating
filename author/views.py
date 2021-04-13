from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from post.models import Post
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
    interested_in = list(request.user.interested_in)
    # print(interested_in)
    # print(Author.objects.filter(rock_type__in=interested_in))
    users = Author.objects.filter(rock_type__in=interested_in).exclude(username=request.user.username)
    matches = Author.objects.all().exclude(username=request.user.username)
    context = {
        "users": users,
        "matches": matches
    }
    return render(request, "explore.html", context)


def admire_view(request, user_id):
    admire_user = Author.objects.get(id=user_id)
    admirer = Author.objects.get(id=request.user.id)
    if admire_user not in admirer.admirers.all():
        admirer.admirers.add(admire_user)
        admirer.save()
    else:
        admirer.admirers.remove(admire_user)
        admirer.save()
    return redirect(reverse("explore"), args=[user_id])
