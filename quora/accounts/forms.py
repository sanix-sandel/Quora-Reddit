from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    email=forms.EmailField()
    password=forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat the same password',
                                widget=forms.PasswordInput)     
    class Meta:
        model=User
        fields=('username',)

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd ['password2']:
            raise forms.ValidationError("passwords don't match")
        return cd['password2']                                                  

