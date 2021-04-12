from django.shortcuts import render
from author.models import Author
# Create your views here.


def author_profile(request, user_id):
    user_obj = Author.objects.get(id=user_id)

    return render(request, "author_detail.html", {
        "author_info": user_obj
    })

