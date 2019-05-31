from django.db import models
from django.core.validators import FileExtensionValidator
from django import forms
import pandas as pd
from django.db import models
# Create your models here.

class Document(models.Model):
    description = models.TextField(max_length=255, blank=True, verbose_name='Descripción')
    name = models.CharField(max_length=128, blank=True, verbose_name='Nombre')
    document = models.FileField(upload_to='files/', verbose_name='Archivo',  validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document_id = models.AutoField(primary_key=True)
    lat_col= models.CharField(max_length=50, null=True, choices={})
    lon_col = models.CharField(max_length=50, null=True, choices={})

#Para traer las columnas *not working*
# def get_cols(self):
#     with open(self.document.path) as fp:
#         df = pd.read_csv(fp)
#         return df.columns

#para agregar otra extensión simplemente hacerlo con ,'json' por ejemplo
#,  validators=[FileExtensionValidator(allowed_extensions=['csv'])]