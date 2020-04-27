from django import forms 
from .models import Question, Answer

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

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer        
        fields=('body',)

    def save(self, commit=True):
        ans=super().save(commit=False)
        body=self.cleaned_data['body']
        if commit:
            ans.save()
        return ans       