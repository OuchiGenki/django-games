from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class Signup(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    next_page = 'othello:index'


class Logout(LogoutView):
    next_page = 'accounts:login'