from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'), 
    path('library/admin/signup/', views.admin_signup, name='admin_signup'),
    path('library/admin/login/', views.admin_login, name='admin_login'),
    path('library/books/', views.view_books, name='view_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('library/user/signup/', views.user_signup, name='user_signup'),
    path('library/user/login/', views.user_login, name='user_login'),
    path('library/user/logout/', views.user_logout, name='user_logout'),
    path('user/home/', views.user_home, name='user_home'),
]



