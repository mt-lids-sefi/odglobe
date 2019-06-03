from django.db import models
from django.core.validators import FileExtensionValidator
from django import forms
import pandas as pd
from django.db import models
# Create your models here.


class Column(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Document(models.Model):
    description = models.TextField(max_length=255, blank=True, verbose_name='Descripción')
    name = models.CharField(max_length=128, blank=True, verbose_name='Nombre')
    document = models.FileField(upload_to='files/', verbose_name='Archivo',  validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document_id = models.AutoField(primary_key=True)
    lat_col = models.ForeignKey(Column, on_delete=models.SET_NULL, null=True, related_name='lat+')
    lon_col = models.ForeignKey(Column, on_delete=models.SET_NULL, null=True, related_name='lon+')

#Para traer las columnas *not working*
    def get_cols(self):
         with open(self.document.path) as fp:
            df = pd.read_csv(fp)
            return df.columns

#para agregar otra extensión simplemente hacerlo con ,'json' por ejemplo
#,  validators=[FileExtensionValidator(allowed_extensions=['csv'])]