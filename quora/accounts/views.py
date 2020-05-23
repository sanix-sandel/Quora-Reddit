from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model=get_user_model()
    form_class=UserChangeForm
    template_name='accounts/profile.html'
    success_url=reverse_lazy('home')
