# from django.contrib import admin

# # Register your models here.
# library_app/admin.py

from django.contrib import admin
from .models import Admin, Book

admin.site.register(Admin)
admin.site.register(Book)

