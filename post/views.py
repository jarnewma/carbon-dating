from django.shortcuts import render, reverse, redirect
from .models import Post
from .models import Author
from post.forms import PostForm
# from .models import NewAdmirer
from django.utils import timezone


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "../templates/post_detail.html", {"post": post})


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            time = timezone.now()
            new_post = Post.objects.create(
                author=Author.objects.get(username=request.user.username),
                caption=data["caption"],
                timestamp=time
            )
            new_post.save()
            return redirect(reverse("homepage"))
    form = PostForm()
    return render(request, "../templates/generic_form.html", {"form": form})
