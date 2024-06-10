from django.urls import path

#implemetar views.py
from . import views

urlpatterns = [

    path('', views.index, name='index'),
]