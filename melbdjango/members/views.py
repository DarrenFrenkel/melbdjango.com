from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.contrib import messages
#from django.db import transaction
#from django.db.utils import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
#from django.views.decorators.http import require_POST
from members.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django import forms
# Create your views here.

def member_registration(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():		
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.backend='django.contrib.auth.backends.ModelBackend'			
            user.save()
            login(request, user)			
            return redirect('/')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})		
	
def member_signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        comment = "Wrong username or password"		
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            hacker = authenticate(username=username, password=password)
            if hacker is not None:
                login(request, hacker)		
                return render(request, 'index.html', {'form':form})
            else:    			
                return render(request, 'index.html', {'form':form, 'comment':comment})
        else:
                return render(request, 'index.html', {'form':form})		
    else:
        form = LoginForm()
        return render(request, 'index.html', {'form':form})		
	

