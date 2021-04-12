from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from author.models import Author


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class AuthorCreationForm(UserCreationForm):

    class Meta:
        model = Author
        fields = ('username',
                  'rock_type',
                  'interested_in',
                  'bio',
                  'birthday',
                  'profilepic')


class AuthorChangeForm(UserChangeForm):

    class Meta:
        model = Author
        fields = ('rock_type',
                  'interested_in',
                  'bio',
                  'birthday',
                  'profilepic')
