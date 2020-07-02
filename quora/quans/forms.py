from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('title', 'body')
    

class AnswerForm(forms.ModelForm):
 #   answer_id=forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model=Answer
        fields=('body',)

    def save(self, commit=True):
        ans=super().save(commit=False)
        body=self.cleaned_data['body']
        if commit:
            ans.save()
        return ans

