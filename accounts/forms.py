from django import forms
from .models import Admin

class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class AdminLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
