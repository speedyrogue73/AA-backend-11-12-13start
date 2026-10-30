from django import forms
from .models import Amir


class CreateAmirform(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


class UpdateAmirform(forms.ModelForm):
    class Meta:
        model = Amir
        fields = ('title', 'content')


class CreateUpdateAmirForm(forms.ModelForm):
    class Meta:
        model = Amir
        fields = ('title', 'content')
