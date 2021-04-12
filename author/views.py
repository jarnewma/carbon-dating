from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from post.models import Post
from author.models import Author
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required
def home_view(request):
    posts = Post.objects.all()[:10]
    context = {
        "posts": posts
    }
    return render(request, 'home.html', context)


def explore_view(request):
    interested_in = list(request.user.interested_in)
    # print(interested_in)
    # print(Author.objects.filter(rock_type__in=interested_in))
    
    users = Author.objects.filter(rock_type__in=interested_in)
    matches = Author.objects.all()
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



# def follow_user(request, user_id):
#     usertofollow = twitteruser.objects.get(id=user_id)
#     currentuser = twitteruser.objects.get(id=request.user.id)
#     if usertofollow not in currentuser.following.all():
#         currentuser.following.add(usertofollow)
#         currentuser.save()
#     else:
#         currentuser.following.remove(usertofollow)
#         currentuser.save()
#     return HttpResponseRedirect(reverse("userinfo", args=[currentuser.id]))