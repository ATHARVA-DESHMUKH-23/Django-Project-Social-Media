from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponse
from django.urls.resolvers import re

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')
    
@login_required(login_url='signin')
def settings(request):
    
    user_profile = Profile.objects.get(user=request.user)
    # TEMP FIX: Set default image if missing
    if not user_profile.profileimg:
        user_profile.profileimg = 'profile_images/blank-profile-picture.png'
        user_profile.save()

    print(user_profile.profileimg)  # Debug print

    return render(request, 'setting.html', {'user_profile': user_profile})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                #login and redirect to account settings
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')    
 
    else:    
        return render(request, 'signup.html')
        
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    return render(request,'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
    
def upload(request):
    return HttpResponse('<h1>Upload Views</h1>')
    
def testing(request):
    if 'num' not in request.session:
        request.session['num'] = 0
    if request.method == 'POST':
        request.session['num'] += 1
    return render(request,'testing.html',{'num':request.session['num']})