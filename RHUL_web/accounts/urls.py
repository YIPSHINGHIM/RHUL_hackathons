from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    # path('login/', LoginView.as_view(template_name='accounts/login.html')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login')

]