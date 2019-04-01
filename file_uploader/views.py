# Create your views here.
import os

import pandas as pd
import geopandas as gpd
import folium
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render, get_object_or_404
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
        filename = fs.save('files/'+myfile.name, myfile)
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

def document_detail(request, pk):
    #en pk viene el id del archivo
    fs = FileSystemStorage()
    document = get_object_or_404(Document, document_id=pk)
    #file = fs.open(document.document)
    #file_url = fs.url(file)
    data = pd.read_csv(document.document)
    data_html = data.to_html(classes='mystyle')
    context = {'document_id': document.document_id, 'document_desc': document.description,
                'data_html': data_html}
    return render(request, 'detail.html', context)

def document_map(request,pk):
    #asumiendo que document es un geojson
    document = get_object_or_404(Document, document_id=pk)
    #leo el geojson con geopandas
    #file = gpd.read_file(document.document)
    mimapa = folium.Map(location=[-34.641552,-58.479811])
    #para cargar un geojson:
    #folium.GeoJson(file).add_to(mimapa)

    #para cargar un csv
    df = pd.read_csv(document.document)
    for index, row in df.iterrows():
        folium.Marker([row['latitude'], row['longitude']],
                      icon=folium.Icon(icon='cloud')
                      ).add_to(mimapa)
    m = mimapa._repr_html_()
    context = { 'map': m , 'name': document.name, 'description': document.description}
    return render(request, 'map.html', context)


class DetailView(generic.DetailView):
    model = Document
    template_name = 'detail.html'


class DocumentsListView(generic.ListView):
    model = Document
    template_name = 'document_list.html'

