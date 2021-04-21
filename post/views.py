from django.shortcuts import render, reverse, redirect
from .models import Post
from .models import Author
from post.forms import PostForm
# from .models import NewAdmirer
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic import DeleteView
from django.urls import reverse_lazy


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "../templates/post/post_detail.html", {"post": post})


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
    return render(request, "../templates/post/post_form.html", {"form": form})


class DeletePost(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('homepage')