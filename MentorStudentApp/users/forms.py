from django import forms
from application.models import AppUser, Role
from django.contrib.auth.forms import UserCreationForm


class AppUserForm(UserCreationForm):
    email = forms.EmailField()
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    role = forms.ModelChoiceField(queryset=Role.objects.all(), widget=forms.Select())
    isIrregular = forms.CheckboxInput()

    class Meta:
        model= AppUser
        fields= ["email", "password1","password2", "role", "isIrregular"]
