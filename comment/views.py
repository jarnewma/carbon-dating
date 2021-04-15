from django.shortcuts import render, reverse, redirect
from .models import Comment
from .models import Author
from .models import Post
from comment.forms import CommentForm
from django.utils import timezone
from django.shortcuts import get_object_or_404


def new_comment(request, id):
    current_post = Post.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            time = timezone.now()
            Comment.objects.create(
                commenter=get_object_or_404(
                    Author,
                    username=request.user.username
                    ),
                content=data["content"],
                post=current_post,
                timestamp=time
            )
            return redirect(reverse("homepage"))
    form = CommentForm()
    return render(
        request,
        "../templates/comments/add_comment.html",
        {"form": form},
        )
