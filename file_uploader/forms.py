from django import forms
from . import models
from django.forms import TextInput, Textarea
import pandas as pd


class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Document
        fields = ('name','description', 'document')
        widgets = {
            'description': Textarea(attrs={'class': '???', 'rows': 5}),
        }

    #Era para completar un dropdown con las columnas. *not working*
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(self.data)
    #     if 'document' in self.data:
    #         try:
    #             fp = open(self.data['document'])
    #             df = pd.read_csv(fp)
    #             print('here')
    #             self.field['lat_col'].queryset= iter(df.columns)
    #             self.field['lon_col'].queryset= iter(df.columns)
    #         except (ValueError, TypeError):
    #             pass