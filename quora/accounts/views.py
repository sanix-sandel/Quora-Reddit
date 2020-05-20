from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from dajngo.views.generic import DetailView, UpdateView

class UserDetail(LoginRequiredMixin, DetailView):
    model=User
    context_object_name='user'
    template_name='accounts/profile.html'
