from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.admin_signup, name='admin_signup'),
    path('login/', views.admin_login, name='admin_login'),


   

]
