from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm

def home(request):
    questions=Question.objects.all()
    context={'questions':questions}
    return render(request, 'quans/home.html', context)

    
def question(request, id):
    question=get_object_or_404(Question, id=id)
    return render(request, 'quans/question.html', {'q':question})

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
# Create your views here.
