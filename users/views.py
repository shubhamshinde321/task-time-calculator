from datetime import datetime
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import auth
from django.contrib import messages
import logging


logger = logging.getLogger(__name__)


def signup(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name').strip()
            email = request.POST.get('email').strip()
            username = request.POST.get('username').strip()
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            exists = CustomUser.objects.filter(username=username).exists()
            if not exists:
                if password == confirm_password:
                    CustomUser.objects.create_user(name=name,
                                                   username=username,
                                                   password=password,
                                                   email=email)
                    messages.success(request, "User Registered Succcesfully")
                    return redirect('users:login')
                else:
                    messages.warning(request, 'Password must match')
                    return redirect('users:signup')
            else:
                messages.warning(request, 'User already exists')
                return redirect('users:signup')
        except Exception as error:
            logger.debug(error)
            messages.warning(request, 'User Creation Failed')
            return redirect('users:signup')
    return render(request, 'users/signup.html')


def login(request):
    year = datetime.now().year
    if request.method == 'POST':
        try:
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            if user is not None:
                auth.login(request, user)
                username1 = request.user.username
                messages.success(request, "Welcome %s" % username1)
                return redirect('user_form:task_form')
            else:
                messages.warning(request, "Username or Password is invalid")
                return redirect('users:login')
        except Exception as error:
            logger.debug(error)
            messages.warning(request, 'Login Failed')
            return redirect('users:signup')
    else:
        return render(request, 'users/login.html', {'year': year})


def logout(request):
    if request.method == 'POST':
        # username = request.user.employee_username
        auth.logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('users:login')
