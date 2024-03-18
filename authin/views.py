from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import * 
from .Forms import *
from django.contrib import messages

def SignIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')    
    
    form = SignInForm()
    return render(request, 'signup.html', {'form': form,'is_in':True})



     
def Login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['pass_word']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'succsec.html',{'user':username})
                
    else:
        form = LoginForm()
    return render(request, 'signup.html', {'form': form,'is_in':False})

def sscc(request):
    
    return render(request,'succsec.html')
