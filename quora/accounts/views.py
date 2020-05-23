from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, UpdateView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#class UserDetail(LoginRequiredMixin, DetailView):
###    template_name='accounts/profile.html'
