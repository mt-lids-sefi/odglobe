from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
  #  path('su/', views.simple_upload, name='simple_upload'),
    path('mu/', views.model_form_upload, name='model_form_upload'),
    path('gallery/', views.gallery, name='gallery'),
    path('documents/', views.DocumentsListView.as_view(), name='documents'),
    path('documents/<pk>/', views.document_detail, name='detail'),
    path('documents_edit/<pk>', views.DocumentUpdate, name='document_update_form'),
    path('documents/map/<pk>', views.document_map, name='map'),
    path('documents/map_lf/<pk>', views.document_map_lf, name='map_lf')
]