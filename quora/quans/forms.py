from django import forms 
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('title', 'body')
    def save(self, commit=True):
        question=super().save(commit=False)
        title=self.cleaned_data['title']
        body=self.cleaned_data['body']
        if commit:
            question.save()    
        return question    