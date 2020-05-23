from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'
