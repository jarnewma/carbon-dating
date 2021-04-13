from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from author.models import Author
from direct_messages.models import Message


# Create your views here.

class MessagesView(LoginRequiredMixin, View):
    def get(self, request, username):
        matched_user = Author.objects.filter(username=username).first()
        messages_recieved = Message.objects.filter(sender=matched_user, receiver=request.user)
        messages_sent = Message.objects.filter(sender=request.user, receiver=matched_user)
        return render(request, "messages/direct_messages.html")

    def post(self, request):
        pass


class AllMessages(LoginRequiredMixin, View):
    def get(self, request):
        user_admiring = request.user.admiring.all()
        user_admirers = request.user.admirers.all()
        matches = user_admiring.intersection(user_admirers)
        return render(request, "messages/messages_preview.html", {"matches": matches})
