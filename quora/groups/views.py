from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Groupe
from .forms import GroupeForm
from quans.models import Question, Answer
from quans.forms import QuestionForm, AnswerForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from quans.forms import QuestionForm
from django.contrib.contenttypes.models import ContentType


class OwnerMixin():
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(owner=[self.request.user])
"""
class GroupeCreateView(LoginRequiredMixin, CreateView):
    model=Groupe
    fields=['title', 'description']
    template_name='groups/create_group.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        try:
            form.instance.owner=self.request.user
            #form.instance.owner=self.request.user
            #retrieve a group and assign the creator to the group of
            #admins
            groupe, created=Group.objects.get_or_create(name='groups_admins')
            #ContentType has also model_class() method that returns the model class
            #represented by this ContentType instance
            self.request.user.groups.add(groupe)
            return super().form_valid(form)
        except:
            return redirect('home')
"""

@login_required
def GroupeCreateView(request):
    if request.method=='POST':
        form=GroupeForm(request.POST)
        if form.is_valid():
            #I put it here because of contentype problem
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            owner=request.user
            new_groupe=Groupe(title=title, description=description,
                owner=owner
            )
            new_groupe.save()
    else:
        form=GroupeForm(request.GET)
    return render(request, 'groups/create_group.html', {'form':form})


class GroupeList(LoginRequiredMixin, ListView):
    model=Groupe
    context_object_name='groups'
    template_name='groups/groups_list.html'


class UserGroupe(LoginRequiredMixin, ListView):
    model=Groupe
    template_name='groups/mygroups.html'
    context_object_name='groups'

    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(member__in=[self.request.user] or owner==request.user)


def join_or_leave(request, id, action):
    groupe=get_object_or_404(Groupe, id=id)
    if action=='join':
        groupe.member.add(request.user)
        group, created=Group.objects.get_or_create(name='groups_members')
        request.user.groups.add(group)
        groupe.save()
    else:
        groupe.member.remove(request.user)
        groupe.save()
    return redirect('home')

def GroupeDetail(request, id):
    groupe=get_object_or_404(Groupe, id=id)
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            newq.submitted_by=request.user
            newq.save()
            return redirect(groupe.get_absolute_url())
    else:
        form=QuestionForm(request.GET)
    return render(request, 'groups/group.html', {'form':form, 'groupe':groupe})
#add member by suggesting him
#remove member from a group
#approve_membership request
#approve member's post(ask question)
#delete_group
#update_group
#following another user ok
#
