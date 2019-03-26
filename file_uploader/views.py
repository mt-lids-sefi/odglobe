# Create your views here.
import os

import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views import generic

from file_uploader.models import Document
from . import forms


def home(request):
    #Acá tengo que subir el archivo
    #return HttpResponse("Hello, you're home.")
    return render(request, 'home.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save('static/'+myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = pd.read_csv(uploaded_file_url)
        data_html = data.to_html()
        #acá rendereo a otra pág
        return render(request, 'simple_upload.html', {'uploaded_file_url': uploaded_file_url, 'data_html': data_html})
    return render(request, 'simple_upload.html')


def gallery(request):
    path='static'  # insert the path to your directory
    img_list =os.listdir(path)
    return render(request, 'gallery.html', {'images': img_list})

def model_form_upload(request):
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

class DocumentsListView(generic.ListView):
    model = Document
    template_name = 'document_list.html'