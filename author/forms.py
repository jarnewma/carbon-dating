from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':":form-control", 'type':'password'}))
    new_password1 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':":form-control", 'type':'password'}))
    new_password2 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':":form-control", 'type':'password'}))

    class Meta:
        model = User
        fields = (
            'Old Password',
            'New Password',
            'Confirmation Password'
        )