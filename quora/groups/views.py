from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Groupe
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group



class GroupeCreateView(LoginRequiredMixin, CreateView):
    model=Groupe
    fields=['title']
    template_name='quans/create_group.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        try:
            form.instance.owner=self.request.user
            #retrieve a group and assign the creator to the group of
            #admins
            groupe, created=Group.objects.get_or_create(name='groups_admins')
            self.request.user.groups.add(groupe)
            return super().form_valid(form)
        except:
            return redirect('home')


class GroupeList(LoginRequiredMixin, ListView):
    model=Groupe
    context_object_name='groups'
    template_name='quans/groups_list.html'


class UserGroupe(LoginRequiredMixin, ListView):
    model=Groupe
    template_name='quans/mygroups.html'
    context_object_name='groups'

    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(members__in=[self.request.user] or owner==self.request.user)


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


#add member by suggesting him
#remove member from a group
#approve_membership request
#approve member's post(ask question)
#delete_group
#update_group
#following another user
#
