# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.lgout, name='logout'),
    path('home_page', views.home_page, name='home_page'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('Admin_home',views.Admin_Home,name='admin_home'),
]
