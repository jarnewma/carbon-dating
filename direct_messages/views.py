from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class MessagesView(LoginRequiredMixin, View):
    def get(self, request, username):
        pass

    def post(self, request):
        pass


class AllMessages(LoginRequiredMixin, View):
    def get(self, request):
        pass
