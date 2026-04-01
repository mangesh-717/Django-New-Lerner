
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', id=user.id)
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile', id=user.id)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    if request.user.id != user.id:
        return redirect('login')  # or handle unauthorized access in some other way
    return render(request, 'profile.html', {'user': user})
