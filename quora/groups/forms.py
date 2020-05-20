from django import forms


class GroupeForm(forms.ModelForm):
    class Meta:
        model=Groupe
        fields=('title',)

    def save(self, commit=True):
        group=super().save(commit=False)
        title=self.cleaned_data['title']
        if commit:
            group.save()
        return group
