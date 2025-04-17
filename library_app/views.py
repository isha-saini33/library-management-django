
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from .forms import AdminSignupForm, AdminLoginForm
from .models import Admin
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserLoginForm


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
                admin.is_staff = True
                admin.save()
                messages.success(request, 'Signup successful! Please login.')
                return redirect('admin_login')
    else:
        form = AdminSignupForm()
    return render(request, 'admin/signup.html', {'form': form})

# Admin Login
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
                    return redirect('view_books')  # Your admin dashboard
                else:
                    messages.error(request, 'Invalid password')
            except Admin.DoesNotExist:
                messages.error(request, 'Admin not found')
    else:
        form = AdminLoginForm()
    return render(request, 'admin/login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash password
            user.save()
            messages.success(request, "Account created! Please log in.")
            return redirect('user_login')
    else:
        form = UserSignupForm()
    return render(request, 'user_signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_home')
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')


def home(request):
    return render(request, 'home.html')


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('view_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books': books})

def edit_book(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('view_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request,book_id ):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('view_books')
    return render(request, 'delete_book.html', {'book': book})

@login_required
def user_home(request):
    from .models import Book
    books = Book.objects.all()
    return render(request, 'user_home.html', {'books': books})



