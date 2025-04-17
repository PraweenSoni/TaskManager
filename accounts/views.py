# accounts/views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ForgetPasswordForm
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
                if user.check_password(password):
                    request.session['user_id'] = user.id
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid password')
            except NormalUser.DoesNotExist:
                messages.error(request, 'Email does not exist')
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
    return redirect('/')

def forgetPass_view(request):
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').strip()
            phone = form.cleaned_data.get('phone').strip()
            new_password = form.cleaned_data.get('new_password').strip()

            # Debug print to ensure correct input values
            print("Reset request received for email:", email, "and phone:", phone)

            user = NormalUser.objects.filter(email=email, phone=phone).first()
            if user:
                old_hash = user.password
                user.set_password(new_password)
                user.save()
                new_hash = user.password
                # Debug prints to verify update
                print("Old password hash:", old_hash)
                print("New password hash:", new_hash)
                print("Password updated correctly?", user.check_password(new_password))
                messages.success(request, "Password updated successfully!")
                return redirect('login')  # or to your appropriate URL
            else:
                messages.error(request, "Invalid email or phone number.")
                return redirect('passwordReset')
        else:
            messages.error(request, "Please correct the errors below.")
            return redirect('passwordReset')
    else:
        form = ForgetPasswordForm()
    return render(request, 'accounts/forget_password.html', {'form': form})