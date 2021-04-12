from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from authentication.forms import AuthorCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from django.views import View

# Create your views here.


class LoginFormView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "registration/login.html", {'form': form})

        def post(self, request):
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(
                    request, username=data['username'], password=data['password'])
                if user:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class SignUpView(CreateView):
    form_class = AuthorCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
