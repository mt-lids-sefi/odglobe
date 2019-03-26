from django.db import models
# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True, verbose_name='Descripción')
    document = models.FileField(upload_to='static/', verbose_name='Archivo')
    uploaded_at = models.DateTimeField(auto_now_add=True)

