from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.views.generic import ListView
from django.db.models import Q


def home(request):
    questions=Question.objects.all()
    context={'questions':questions}
    return render(request, 'quans/home.html', context)


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

@login_required
def submitq(request):
    if request.method=="POST":
        form=QuestionForm(request.POST)
        if form.is_valid():
            newq=form.save(commit=False)
            newq.submitted_by=request.user
            newq.save()
            return redirect (newq.get_absolute_url())
    else:
        form=QuestionForm(request.GET)
    return render(request, 'quans/submission.html', {'form':form})

def upvote(request, id, action):
    answer=get_object_or_404(Answer, id=id)
    if action=='like':
        answer.user_upvote.add(request.user)
        answer.save()
    return redirect('home')


def user_questions(request):
    user=request.user
    questions=user.questions_submitted.all()
    return render(request,
                 'quans/user_questions.html',
                  {'questions':questions})


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
