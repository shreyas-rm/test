from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *

def signin(request):
    template = 'users/login.html'
    
    if ('page_type_action' in request.session.keys()) and not request.session['page_type_action']:
        request.session['error'] = None
    
    request.session['page_type_action'] = False
    
    return render(request,template)

def actionLogin(request):
    page = 'users-login'
    
    request.session['error'] = None
    
    if request.method == "POST":
        status = True
        
        for each in ['email','password']:
            if each not in request.POST.keys():
                status = False
                break
        
        if status:
            email = request.POST['email']
            password = request.POST['password']
            
            user = authenticate(username=email, password=password)
            
            if user is not None and user.is_active:
                login(request, user)
                page = 'portal-dashboard'
            
            else:
                request.session['error'] = "Invalid email and/or password"
        
        else:
            request.session['error'] = "Please complete all required fields"
        
    else:
        request.session['error'] = "Invalid request type"
    
    request.session['page_type_action'] = True
    
    return redirect(page)

@login_required
def signout(request):
    logout(request)
    
    return redirect('users-login')