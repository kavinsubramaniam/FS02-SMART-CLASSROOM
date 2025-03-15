from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Import User model
from django.contrib.auth.hashers import make_password  # Import for password hashing
from student_app.models import Student
from teacher_app.models import Teacher

from .forms import StudentForm, TeacherForm

def home(request):
    return render(request, 'auth_app/home.html')

def login(request):
    
    
    return render(request, 'auth_app/login.html')


def register(request):

    
    
    return render(request, 'auth_app/register.html')


