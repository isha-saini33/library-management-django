from django import forms
from .models import Book
from .models import Admin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class AdminLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn']

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
