from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:     # gives us a nested namespace for configurations and keeps them in same place
        model = User
        fields = ['username', 'email', 'password1', 'password2']
