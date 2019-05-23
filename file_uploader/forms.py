from django import forms
from . import models
from django.forms import TextInput, Textarea

class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Document
        fields = ('name','description', 'document' )
        widgets = {
            'description': Textarea(attrs={'class': '???', 'rows': 5}),
        }