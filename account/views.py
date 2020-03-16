from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .form import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            user.account.active = True
            user.save()
            return redirect('update_profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def update(request):  # CON PHAN THEM AVATAR, FIRST NAME VA LAST NAME
    if my_view and request.method == 'POST':
        form = UserUpdateForm(request.POST)
        user = User.objects.get(username=request.user)
        if form.is_valid():
            user.account.firstname = request.POST['firstname']
            user.account.lastname = request.POST['lastname']
            user.account.phone = request.POST['phone']
            user.account.room = request.POST['room']
            user.account.dob = request.POST['dob']
            user.save()
            return render(request, 'update_successfully.html')  # EM CHUA BIET REDIRECT DI DAU
    else:
        form = UserUpdateForm()
    return render(request, 'my_account.html', {'form': form})



def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
        user.account.active = True
        user.save()
    args = {'user': user}
    return render(request, 'my_profile.html', args)

def loguserout(request):
    user = request.user
    user.account.active = False
    user.save()
    logout(request)
    return redirect('home')

def members(request):
    members = User.objects.all()
    return render(request, 'members.html', {'members': members})
