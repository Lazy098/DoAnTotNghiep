from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Course
import json

def regis(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username=username, password=password, email=email)
        return redirect('login')
    return render(request, 'regis.html')

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if username == "nam1":
                return redirect("adm")
            else:
                return redirect('homepage')
        else:
            return redirect('login')
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')

def adm(request):
    return render(request, 'admin.html')

def timer(request):
    return render(request, 'timer.html')

def cou(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    for course in courses:                                                             #cai nay khi dung sang trang khac thi copy nguyen si no vao 
        contents = json.loads(course.contents)
        course.contents = contents
    return render(request,'course.html', context)

def users(request):
    users = User.objects.all()  # Retrieve all user objects from the database
    return render(request, 'user_admin.html', {'users': users})

def cou_adm(request):
    return render(request,'courses_admin.html')

def rp_adm(request):
    return render(request,'reports_admin.html')

def about(request):
    return render(request,'about.html')

def detail(request, course_id):
    courses = Course.objects.filter(id=course_id)
    context = {"courses": courses, "course_id":course_id}
    for course in courses:                                                             #cai nay khi dung sang trang khac thi copy nguyen si no vao 
        contents = json.loads(course.contents)
        course.contents = contents
    return render(request,'detail.html', context)

def prof(request):
    return render(request,'profile.html')