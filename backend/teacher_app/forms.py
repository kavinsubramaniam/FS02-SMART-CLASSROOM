from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Teacher


class TeacherForm(UserCreationForm):

    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Teacher
        fields = ['username', 'email']