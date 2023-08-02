from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .models import Formregister


# Create your views here.


def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect(login)
        else:
            messages.info(request, "Password not matching")
            return redirect(register)
    return render(request, "register.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(notify)
        else:
            messages.info(request, "Invalid username or password")
            return redirect(login)
    return render(request, "login.html")


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        address = request.POST.get('address', '')
        dob = request.POST.get('dob', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        district = request.POST.get('district', '')
        branch = request.POST.get('branch', '')
        type = request.POST.get('type', '')
        materials = request.POST.get('materials','')
        form=Formregister(name=name,address=address,dob=dob,age=age,gender=gender,phone=phone,email=email,district=district,branch=branch,type=type,materials=materials)
        form.save()
        return redirect(msg)
    return render(request,'form.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def refresh(request):
    return render(request,"index.html")

def msg(request):
    return render(request,"msg.html")

def notify(request):
    return render(request,"notify.html")