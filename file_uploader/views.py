# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from wq.io import load_file
import pandas as pd


def home(request):
    #Acá tengo que subir el archivo
    #return HttpResponse("Hello, you're home.")
    return render(request, 'home.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save('files/'+myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = pd.read_csv(uploaded_file_url)
        data_html = data.to_html()
        #acá rendereo a otra pág
        return render(request, 'simple_upload.html', {'uploaded_file_url': uploaded_file_url, 'data_html': data_html})
    return render(request, 'simple_upload.html')
