from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from post.models import Post
from author.models import Author
from django.contrib.auth.decorators import login_required
from authentication.forms import AuthorChangeForm
# Create your views here.


@login_required
def author_profile(request, user_id):
    user_obj = Author.objects.get(id=user_id)
    user_posts = Post.objects.all().filter(author=user_obj)
    context = {
        "author_info": user_obj,
        "posts": user_posts
    }

    return render(request, "author_detail.html", context)


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


def profile_admire_view(request, user_id):
    admire_user = Author.objects.get(id=user_id)
    admirer = Author.objects.get(id=request.user.id)
    if admire_user not in admirer.admirers.all():
        admirer.admirers.add(admire_user)
        admirer.save()
    else:
        admirer.admirers.remove(admire_user)
        admirer.save()
    return HttpResponseRedirect(reverse("author_profile", args=[user_id]))


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "../templates/author_detail.html", {"post": post})


@login_required
def change_profile(request):
    if request.method == "POST":
        form = AuthorChangeForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.profilepic = request.FILES['profilepic']
            form.save()
        return HttpResponseRedirect(reverse("author_profile", args=[request.user.id]))
    form = AuthorChangeForm(initial={
        'rock_type': request.user.rock_type,
        "interested_in": request.user.interested_in,
        "bio": request.user.bio,
        "password":request.user.password
        
    })
    return render(request, "generic_form.html",{"form":form})
    