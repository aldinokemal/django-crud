from django import forms
from django.core import validators
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'type': 'text', 'class': 'input'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'input'}),
            'password': forms.TextInput(attrs={'type': 'password','class': 'input'}),
        }