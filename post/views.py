from django.shortcuts import render, reverse, redirect
from .models import Post
from .models import Author
from post.forms import PostForm
# from .models import NewAdmirer
from django.utils import timezone
from django.shortcuts import get_object_or_404


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "../templates/post_detail.html", {"post": post})


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            time = timezone.now()
            new_post = Post.objects.create(
                author=get_object_or_404(
                    Author,
                    username=request.user.username
                    ),
                caption=data["caption"],
                image=data['image'],
                timestamp=time
            )
            new_post.save()
            return redirect(reverse("homepage"))
    form = PostForm()
    return render(request, "../templates/generic_form.html", {"form": form})
