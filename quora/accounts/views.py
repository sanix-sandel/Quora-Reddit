from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MyUser, Contact

class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model=get_user_model()
    form_class=UserChangeForm
    template_name='accounts/profile.html'
    success_url=reverse_lazy('home')

def See_Profile(request, id):#we can also CBV
    user=get_object_or_404(MyUser, id=id)

    return render(request, 'accounts/see_profile.html', {'user':user})


def follow(request, id):
    user=get_object_or_404(MyUser, id=id)
    Contact.objects.get_or_create(user_form=request.user, user_to=user)
    return redirect('top_publishers')
