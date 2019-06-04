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



class DocumentFormCols(forms.Form):
    class Meta:
        model = models.Document
    
    lat_col = forms.ChoiceField(choices=Meta.model.get_cols(Meta.model))
    lon_col = forms.ChoiceField(choices=Meta.model.get_cols(Meta.model))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #self.fields['lat_col'].queryset = self.Meta.model.get_cols(self.Meta.model)
        #self.fields['lon_col'].queryset = self.Meta.model.get_cols(self.Meta.model)
        

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