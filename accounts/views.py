from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import AdminSignupForm, AdminLoginForm
from .models import Admin
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Admin.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
            else:
                admin = form.save(commit=False)
                admin.password = make_password(form.cleaned_data['password'])
                admin.save()
                messages.success(request, 'Signup successful! Please login.')
                return redirect('admin_login')
    else:
        form = AdminSignupForm()
    return render(request, 'signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                admin = Admin.objects.get(email=email)
                if check_password(password, admin.password):
                    request.session['admin_id'] = admin.id
                    messages.success(request, 'Login successful!')
                    return redirect('view_books')  # redirect to some dashboard page
                else:
                    messages.error(request, 'Invalid password')
            except Admin.DoesNotExist:
                messages.error(request, 'Admin not found')
    else:
        form = AdminLoginForm()
    return render(request, 'login.html', {'form': form})

