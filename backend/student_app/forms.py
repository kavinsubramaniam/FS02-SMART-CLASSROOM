from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Student


class StudentForm(UserCreationForm):

    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Student
        fields = ['username', 'email']