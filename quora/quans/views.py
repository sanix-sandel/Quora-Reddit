from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView
)   
from django.views.generic.base import View
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from actions.utils import create_action
from actions.utils import create_notification
import redis
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse

from api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view




#Connection to redis
r=redis.Redis(host=settings.REDIS_HOST,
             port=settings.REDIS_PORT,
             db=settings.REDIS_DB)


#class home(ListView):
#    model=Question
#    context_object_name='questions'
#    template_name='quans/home.html'

#    def get_queryset(self):
#        qs=super().get_queryset()
#        return qs.filter(groupe=None, groups_request=None)

def home(request):
    questions=Question.objects.filter(groupe=None, groups_request=None)
    form=QuestionForm()
    context={
        'questions':questions,
        'form':form
    }
    return render(request, 'quans/home.html', context)

class OwnerMixin():
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(submitted_by=self.request.user)



def question(request, id):
    question=get_object_or_404(Question, id=id)
    ans=question.answers.all()
    views=r.incr(f'question:{question.id}:views')#for redis
                  #object-type:id:field
    ansform=AnswerForm()
    if request.method=='POST':
        form=AnswerForm(request.POST)    
        return valider(request, form, question)    
    else:
        form=AnswerForm(request.GET)
    return render(request, 'quans/question.html',
                 {'q':question, 'ans':ans, 'form':form, 
                 'views':views, 'ansform':ansform})


@login_required
def valider(request, form, question):
    if form.is_valid():
        newa=form.save(commit=False)
        newa.submitted_by=request.user
        newa.reply_to=question
        user1=question.submitted_by
        newa.save()
        create_notification('replied to your question', user1, user=request.user)
        return redirect(question.get_absolute_url())


"""
class submitq(LoginRequiredMixin, CreateView):
    model=Question
    fields=['title', 'body']
    template_name='quans/submission.html'
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        form.instance.submitted_by=self.request.user
        target=super().form_valid(form)
        return target
"""

@login_required
def submitq(request, id=None):
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            body=form.cleaned_data['body']
            newq=Question(title=title, body=body,
                submitted_by=request.user
            )
            newq.save()
            create_action(request.user,
                'asked a new question', newq
            )
            return redirect('home')
    else:
        form=QuestionForm()
    return render(request, 'quans/submission.html', {'form':form})



class editq(OwnerMixin, LoginRequiredMixin, UpdateView):
    model=Question
    fields=['title', 'body']
    template_name='quans/submission.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.submitted_by=self.request.user
        return super().form_valid(form)



@login_required
def retwitter(request, qi):
    q=get_object_or_404(Question, id=qi)

    try:
        q.retwitters.add(request.user)
        q.save()
        return redirect('home')
    except:
        return redirect('home')


class edita(OwnerMixin, LoginRequiredMixin, UpdateView):
    model=Answer
    fields=('body',)
    template_name='quans/edita.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.submitted_by=self.request.user
        return super().form_valid(form)



class deleteq(OwnerMixin, LoginRequiredMixin, DeleteView):
    model=Question
    success_url=reverse_lazy('user_questions')
    template_name='quans/deleteq.html'


@login_required
def upvote(request, id, action):
    answer=get_object_or_404(Answer, id=id)
    #if action=='like':#we have to remove this condition
    if request.user in answer.user_upvote.all():
        answer.user_upvote.remove(request.user)
    else:
        #increment answer ranking with a sorted set
        #A sorted set is is a non-repeating collection of
        #strings in which every member is associated with score
        answer.user_upvote.add(request.user)
        #likes=r.incr(f'answer:{answer.id}:likes')
        #r.zincrby('answer_ranking', 1, anwer.id)
        user1=answer.submitted_by
        create_notification('liked your answer', user1, user=request.user)
    answer.save()

    return redirect('question', id=answer.reply_to.id)

#The zincrby() is used to store answer ranking(likes) nin a sorted

#
#def answer_ranking(request):
    #get the answer ranking dictionnary
    #Obtain the elements in the sorted set
#    answer_ranking=r.zrange('answer_ranking', 0, -1, desc=True)[:10]
#    answer_ranking_ids=[int(id) for id in answer_ranking]
    #get most ranked answer
#    most_ranked=list(Answer.objects.filter(id__in=answer_ranking_ids))
#    most_ranked.sort(key=lambda x:answer_ranking_ids.index(x.id))
#    return render(request, )




class user_questions(OwnerMixin, LoginRequiredMixin, ListView):
    model=Question
    context_object_name='questions'
    template_name='quans/user_questions.html'



@login_required
def user_answers(request):
    user=request.user
    answers=user.user_answers.all()
    return render(request, 'quans/user_answers.html',
                 {'answers':answers})



class searchquestions(ListView):
    model=Question
    context_object_name='questions_searched'
    template_name='quans/search_results.html'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Question.objects.filter(
            Q(title__icontains=query)|Q(body__icontains=query)
        )

@api_view(['POST'])
def ask(request, *args, **kwargs):
    serializer=QuestionSerializer(data=request.POST)
    print('life')
    if serializer.is_valid(raise_exception=True):
        serializer.save(submitted_by=request.user)
        print('yo')
        return Response(serializer.data, status=201)
    print('yeah')    
    return Response({}, status=400)          