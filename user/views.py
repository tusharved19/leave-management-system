from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from emp.models import *
from .forms import UserLogin, UserForm
#from user.models import Employee


def register_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            username = form.cleaned_data['username']

            messages.success(request,'account created for{0}'.format(username))
            return redirect('user:register')

        else:
            messages.errors(request, 'invalid username')
            return redirect('user:register')

    form = UserForm()
    dataset = dict()
    dataset['form'] = form
    dataset['title'] = 'register user'
    return render(request, 'user/register.html', dataset)


def login_view(request):
    login_user = request.user

    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user and user.is_active:
                login(request, user)
                if login_user.is_authenticated:
        	        return redirect('dashboard:dashboard')
            else:
        	    messages.error(request, 'Account is invalid')
            return redirect('user:login')

        else:
	        return HttpResponse('data not valid')


    dataset = dict()
    form = UserLogin()
    dataset['form'] = form
    return render(request, 'user/login.html', dataset)


def users_list(request):
    employees = Employee.object.all()
    return render(request, 'user/users_table.html',{'employees':employees,'title':'users list'})

def logout_view(request):
    logout(request)
    return redirect('user:login')

