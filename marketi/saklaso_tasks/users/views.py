from django.shortcuts import render, redirect
from .forms import UserRegisterForm,UserLoginForm, authanticate
from django.contrib.auth import login, authenticate, logout


def register_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save
            username = form.cleaned_data.get('username')
            return redirect('home')


    return render(request, 'user_form.html')

def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')


    return render(request, 'user_form.html')

def logout_view(request):
    logout(request)

    return redirect('login_view')