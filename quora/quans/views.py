from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class home(ListView):
    model=Question
    context_object_name='questions'
    template_name='quans/home.html'



class OwnerMixin():
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(submitted_by=self.request.user)



def question(request, id):
    question=get_object_or_404(Question, id=id)
    ans=question.answers.all()
    if request.method=='POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            newa=form.save(commit=False)
            newa.submitted_by=request.user
            newa.reply_to=question
            newa.save()

            return redirect(question.get_absolute_url())
    else:
        form=AnswerForm(request.GET)
    return render(request, 'quans/question.html',
                 {'q':question, 'ans':ans, 'form':form})




class submitq(LoginRequiredMixin, CreateView):
    model=Question
    fields=['title', 'body']
    template_name='quans/submission.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.submitted_by=self.request.user
        return super().form_valid(form)


class editq(OwnerMixin, LoginRequiredMixin, UpdateView):
    model=Question
    fields=['title', 'body']
    template_name='quans/submission.html'
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
    if action=='like':
        answer.user_upvote.add(request.user)
        answer.save()
    return redirect('home')


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
            Q(title__contains=query)|Q(title__icontains=query)
        )
# Create your views here.
