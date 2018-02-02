from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    email_address = forms.CharField(required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email_address', 'password1', 'password2')