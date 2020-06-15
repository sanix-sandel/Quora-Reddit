from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django import forms

class UserCreationForm(forms.ModelForm):

    password1=forms.CharField(label='password', widget=forms.PasswordInput)
    password2=forms.CharField(label='password confirmation', widget=forms.PasswordInput)

    class Meta:
        model=get_user_model()
        fields=('username', 'email', 'date_of_birth')

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password don't match")
        return password2

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()

    class Meta:
        model=get_user_model()
        fields=('username', 'email', 'date_of_birth', 'profile_image', 'about')

#    def clean_password(self):
#        return self.initial['password']
