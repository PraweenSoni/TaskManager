# accounts/views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import NormalUser
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']  # hashing should be added
            user.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = NormalUser.objects.get(email=email)
                if user.password == password:
                    request.session['user_id'] = user.id
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid password')
            except NormalUser.DoesNotExist:
                messages.error(request, 'User does not exist')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def dashboard_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = NormalUser.objects.get(id=user_id)
    return render(request, 'accounts/dashboard.html', {'user': user})


def logout_view(request):
    request.session.flush()
    return redirect('login')
