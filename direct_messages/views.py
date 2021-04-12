from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from author.models import Author


# Create your views here.

class MessagesView(LoginRequiredMixin, View):
    def get(self, request, username):
        return render(request, "messages/direct_messages.html")

    def post(self, request):
        pass


class AllMessages(LoginRequiredMixin, View):
    def get(self, request):
        user_admiring = request.user.admiring.all()
        user_admirers = request.user.admirers.all()
        matches = user_admiring.intersection(user_admirers)
        return render(request, "messages/messages_preview.html", {"matches": matches})
