from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True, verbose_name='Descripción')
    name = models.CharField(max_length=128, blank=True, verbose_name='Nombre')
    document = models.FileField(upload_to='files/', verbose_name='Archivo',  validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document_id = models.AutoField(primary_key=True)

#para agregar otra extensión simplemente hacerlo con ,'json' por ejemplo
#,  validators=[FileExtensionValidator(allowed_extensions=['csv'])]