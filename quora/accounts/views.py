from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView
)
from .forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MyUser, Contact
from actions.models import Action
from actions.utils import create_notification


class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model=get_user_model()
    form_class=UserChangeForm
    template_name='accounts/profile.html'
    success_url=reverse_lazy('home')
"""
class TopPublishersView(ListView):
    model=MyUser
    context_object_name='users'
    template_name='account/top_publishers.html'
"""
def See_Profile(request, id):#we can also CBV
    user=get_object_or_404(MyUser, id=id)

    return render(request, 'accounts/see_profile.html', {'user':user})



def follow(request, id):
    user1=get_object_or_404(MyUser, id=id)
    Contact.objects.create(user_from=request.user, user_to=user1)
    create_notification('follows you', user1, user=request.user)
    return redirect('home')#'top_publishers')
#def unfollow

def notifications(request):
    #Display all actions by default
    actions=Action.objects.exclude(user=request.user)
    #the id of the user's followings
    following_ids=request.user.following.values_list('id', flat=True)
    #flat=True means that the returned results are single values rather than
    #one-tuples

    if following_ids:
        #if user is following ohers, retrieve only their actions
        actions=actions.filter(user_id__in=following_ids)
    actions=actions.select_related('user').prefetch_related('target')[:10]

    return render(request, 'accounts/notifications.html', {'actions':actions})


def personal_notifications(request):
    user=request.user
    notifications=Notification.objects.filter(target=request.user)
    return render(request, 'accounts/notifications.html',
                    {'notifications':notifications})
