from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from author.models import Author
from direct_messages.models import Message


# Create your views here.

class MessagesView(LoginRequiredMixin, View):
    def get(self, request, username):
        matched_user = Author.objects.filter(username=username).first()
        messages_received = Message.objects.filter(
            sender=matched_user, receiver=request.user)
        messages_received.update(viewed=True)
        messages_sent = Message.objects.filter(
            sender=request.user, receiver=matched_user)
        messages = messages_sent.union(
            messages_received).order_by("created_at")
        return render(request, "messages/direct_messages.html", {"messages": messages,
                                                                 "profile_pic": matched_user.profilepic})

    def post(self, request, username):
        content = request.POST.get("content")
        matched_user = Author.objects.filter(username=username).first()
        Message.objects.create(sender=request.user,
                               receiver=matched_user, content=content)
        return HttpResponseRedirect(request.path)


class AllMessages(LoginRequiredMixin, View):
    def get(self, request):
        unread_messages = Message.objects.filter(
            receiver=request.user, viewed=False).order_by('-created_at')
        read_messages = Message.objects.filter(
            receiver=request.user, viewed=True).order_by('-created_at')
        user_admiring = request.user.admiring.all()
        user_admirers = request.user.admirers.all()
        matches = user_admiring.intersection(user_admirers)
        return render(request, "messages/messages_preview.html", {"matches": matches,
                                                                  "unread_messages": unread_messages,
                                                                  "read_messages": read_messages})
