from django import forms
from django.forms import TextInput, Textarea
from . import models

class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Document
        fields = ('name','description', 'document' )
        widgets = {
            'description': Textarea(attrs={'class': '???', 'rows': 5}),
        }