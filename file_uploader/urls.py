from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('su/', views.simple_upload, name='simple_upload'),
    path('mu/', views.model_form_upload, name='model_form_upload'),
    path('gallery/', views.gallery, name='gallery'),
    path('documents/', views.DocumentsListView.as_view(), name='documents')
]