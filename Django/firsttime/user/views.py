from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import Course, Feedback
import json
from django.contrib.auth.hashers import make_password

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

def feedback_adm(request):
    customer_feedback = Feedback.objects.all()
    return render(request,'feedback_admin.html', {'customer_feedback': customer_feedback})

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

def feedback(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_description = request.POST['user_description']
        feedback_infor = Feedback.objects.create(user_name=user_name, user_feedback=user_description)
        feedback_infor.save()
    return render(request,'feedback.html')

def setting(request):
    return render(request,'setting.html')

def update_users(request, post_id):
    post = get_object_or_404(User, id=post_id)

    if request.method == 'POST':
        edit_form = UserForm(request.POST, instance=post)
        if edit_form.is_valid():
            user = edit_form.save(commit=False)
            password = request.POST.get('password')
            user.password = make_password(password)  # Set the new password using set_password method
            user.save()
            return redirect('users')

    return render(request, 'edit_user.html', {'edit_form': edit_form, 'post_id': post_id})