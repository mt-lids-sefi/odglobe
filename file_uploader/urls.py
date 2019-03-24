from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('su/', views.simple_upload, name='simple_upload'),

]