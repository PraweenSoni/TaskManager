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

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=15)
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)