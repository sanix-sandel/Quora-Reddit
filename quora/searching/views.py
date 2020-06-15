from django.db.models import Q
from django.shortcuts import render
from quans.models import Question
from django.views.generic import ListView

class Search(ListView):
    model=Question
    template_name='searching/results.html'
    context_object_name='results'

    def get_queryset(self):
     #   q=super().get_queryset()
    #    print(self.request.GET)

        query=self.request.GET.get('q')
        return Question.objects.filter(
            Q(title__icontains=query)|Q(body__icontains=query)|Q(submitted_by__username__icontains=query)
        )
