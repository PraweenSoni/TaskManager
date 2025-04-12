# accounts/forms.py
from django import forms
from .models import NormalUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = NormalUser
        fields = ['email', 'password', 'phone']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
