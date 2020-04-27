from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm


def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(
                form.cleaned_data['password']
            )
            user.save()
        
            return redirect('login')
    else:
        form=UserRegistrationForm(request.GET)
    return render(request, 'accounts/register.html', {'form':form})  



def login_view(request):
    form=AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user=form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/login.html', {'form':form})           
# Create your views here.


def logout_view(request):
    user=request.user
    logout(request)
    return redirect ('login')