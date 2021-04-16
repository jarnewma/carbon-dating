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
            else:
                return render(request, "registration/login.html",
                              {"form": form,
                               "message": "Wrong username or password, please try again"})
        return render(request, "registration/login.html",
                      {"form": form,
                               "message": "Missing fields"})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class SignUpView(CreateView):
    form_class = AuthorCreationForm
    success_url = '/'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)

        login(self.request, self.object)
        return valid
