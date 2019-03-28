from django.db import models
# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True, verbose_name='Descripción')
    document = models.FileField(upload_to='files/', verbose_name='Archivo')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document_id = models.AutoField(primary_key=True)