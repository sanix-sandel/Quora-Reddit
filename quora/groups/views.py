from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Groupe, MembersRequested, QuestionRequestList
from .forms import GroupeForm
from quans.models import Question, Answer
from quans.forms import QuestionForm, AnswerForm
from actions.models import Action, Notification
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
from django.conf import settings
from accounts.models import MyUser
from .forms import GroupeForm
from actions.utils import create_action


class OwnerMixin():
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(owner=[self.request.user])



class Member():
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.only("member")



class Questions(ListView):
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.questions.all



@login_required
def GroupeCreateView(request):
    if request.method=='POST':
        form=GroupeForm(request.POST)
        if form.is_valid():
            #I put it here because of contentype problem
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            private=form.cleaned_data['private']
            owner=request.user
            new_groupe=Groupe(title=title, description=description,
                owner=owner, private=private
            )
            group, created=Group.objects.get_or_create(name='groups_admins')
            #groupe, created=Group.objects.get_or_create(name='groups_admins')
            request.user.groups.add(group)#add the creator to admin group
            new_groupe.save()
            new_groupe.member.add(owner)#add the creator as a member
            #owner.groups.add(groupe)
            return redirect('list_groups')
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
        return qs.filter(member__in=[self.request.user])


def join_or_leave(request, id, action):
    groupe=get_object_or_404(Groupe, id=id)
    if action=='join':
        if groupe.private:
            create_action(request.user, ' wants to join ', groupe)
            groupe.membersrequested.members.add(request.user)
            groupe.save()
        else:
            groupe.member.add(request.user)
            group, created=Group.objects.get_or_create(name='groups_members')
            request.user.groups.add(group) #add the user to membership group
            groupe.save()
            return redirect('groupe_detail', groupe.id)
    else:
        groupe.member.remove(request.user)
        groupe.save()
    return redirect('list_groups')



def GroupeDetail(request, id):
    groupe=get_object_or_404(Groupe, id=id)
    members=groupe.member.all()
    members_request=get_object_or_404(MembersRequested, groupe=groupe).members.all()
    questions_request=get_object_or_404(QuestionRequestList, groupe=groupe).questions.all()
    questions=Question.objects.filter(groupe=groupe)
    print(questions)
    if request.user in members or request.user==groupe.owner:
        if request.method=='POST':
            form=QuestionForm(request.POST)
            if form.is_valid():
                newq=form.save(commit=False)
                newq.submitted_by=request.user
                questionrequestlist=get_object_or_404(QuestionRequestList,
                groupe=groupe)

                #newq.groupe=groupe
                
                if groupe.owner==request.user or not groupe.private:
                    newq.groupe=groupe
                    newq.save()
                    
                else:
                    
                    newq.save()
                    print('savedooo')
                    questionrequestlist.questions.add(newq)
                    questionrequestlist.save()
                print(newq)
                return redirect(groupe.get_absolute_url())
        else:
            form=QuestionForm()
        return render(request, 'groups/group.html',
                {'form':form,
                'groupe':groupe,
                'members':members,
                'members_request':members_request,
                'questions_request':questions_request})
    else:
        return redirect('list_groups')


def GroupeMemberList(request, id):
    groupe=get_object_or_404(Groupe, id=id)
    is_owner=request.user==groupe.owner
    
    return render(request, 'groups/membergroupe.html',
                 {'groupe':groupe, 'is_owner':is_owner})



def RemoveMember(request, id, g_id):
    user=get_object_or_404(MyUser, id=id)
    groupe=get_object_or_404(Groupe, id=id)
    groupe.member.remove(user)
    groupe.save()
    return redirect('groupe_members', id=g_id)


class UpdateGroupe(LoginRequiredMixin, UpdateView):
    model=Groupe
    fields=['title', 'description']
    template_name='groups/updateg.html'
    success_url=reverse_lazy('list_groups')

    def form_valid(self, form):
        form.instance.submitted_by=self.request.user
        return super().form_valid(form)



class DeleteGroupe(LoginRequiredMixin, DeleteView):
    model=Groupe
    success_url=reverse_lazy('home')
    template_name='groups/deleteg.html'



def GroupeActivities(request, id):
    groupe=get_object_or_404(Groupe, id=id)
    actions=Action.objects.filter(target_id=groupe.id)
    #Problem solved, must use target_id insted of just target
    return render(request, 'groups/activities.html', {'actions':actions})
    #return render(request, 'groups/activities.html')

#add member by suggestion


#class MembershipRequest(LoginRequiredMixin, ListView):


@login_required
def MembershipRequest(request, group_id):
    groupe=get_object_or_404(Groupe, id=group_id)
    members=MembersRequested.objects.get(groupe=groupe).members.all()
    return render(request, 'groups/membersrequest.html',
                {'members':members, 'groupe':groupe})


@login_required
def QuestionRequest(request, group_id):
    groupe=get_object_or_404(Groupe, id=group_id)
    questions=QuestionRequestList.objects.get(groupe=groupe).questions.all()
    return render(request, 'groups/questionsrequest.html',
                    {'questions':questions, 'groupe':groupe})



def accept_member(request, group_id, user_id):
    user=get_object_or_404(MyUser, id=user_id)
    groupe=get_object_or_404(Groupe, id=group_id)
    groupe.member.add(user)
    #get the members request list
    request_list=get_object_or_404(MembersRequested, groupe=groupe)
    request_list.members.remove(user)#Remove the new member from
    #members request list
    return redirect('membership_request', group_id=groupe.id)


def approve_question(request, group_id, question_id):
    groupe=get_object_or_404(Groupe, id=group_id)
    questionrequestlist=get_object_or_404(QuestionRequestList, groupe=groupe)
    question=get_object_or_404(Question, id=question_id)
    groupe.questions.add(question)
    questionrequestlist.questions.remove(question)
    return redirect('question_request_list', group_id=groupe.id)
#approve member's post(ask question)


#
def shared(request, q_id, g_id):
    question=get_object_or_404(Question, id=q_id)
    groupe=get_object_or_404(Groupe, id=g_id)
    question.groupe=groupe
    question.save()
    return redirect('home')