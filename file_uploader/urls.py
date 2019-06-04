from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mu/', views.model_form_upload, name='model_form_upload'),
    path('documents/', views.DocumentsListView.as_view(), name='documents'),
    path('documents/<pk>/', views.document_detail, name='detail'),
    #path('documents/map/<pk>', views.document_map, name='map'),
    path('documents/map_lf/<pk>', views.document_map_lf, name='map_lf'),
    path('document/<int:pk>/update', views.DocumentUpdateView.as_view(),name='document_update_form'),
    #path('document/<int:pk>/cols', views.DocumentUpdateCols.as_view(),name='document_update_cols')
    path('document/<int:pk>/cols', views.cols_form_upload ,name='document_update_cols'),
    path('ajax/load-cities/', views.load_cols, name='ajax_load_cols'),  # <-- this one here
]