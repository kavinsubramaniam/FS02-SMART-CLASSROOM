from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Import User model
from django.contrib.auth.hashers import make_password  # Import for password hashing
from student_app.models import Student
from teacher_app.models import Teacher

def home(request):
    return render(request, 'home_app/home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Use `.get()` to avoid KeyError
        password = request.POST.get('password')

        print(email, password)
        return redirect('home')  # Redirect instead of rendering

    return render(request, 'home_app/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        designation = request.POST.get('designation')

        # Save the user details in the session
        request.session['name'] = name
        request.session['email'] = email
        request.session['designation'] = designation

        return redirect('password')  # Redirect to password page

    return render(request, 'home_app/register.html')

def password(request):
    if request.method == "POST":
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'home_app/password.html', {"error": "Passwords do not match"})

        name = request.session.get('name')
        email = request.session.get('email')
        designation = request.session.get('designation')

        if not name or not email or not designation:
            return redirect('register')

        # Hash password and create a User object
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        # Create Student or Teacher linked to User
        if designation == "student":
            Student.objects.create(user=user, name=name, email=email)
        else:
            Teacher.objects.create(user=user, name=name, email=email)

        request.session.flush()  
        return redirect('home')  

    return render(request, 'home_app/password.html')
