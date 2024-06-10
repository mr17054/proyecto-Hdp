from django.urls import path




#implemetar views.py
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    #path('', views.index, name='index'),

    #registrarse
    path("signup/", views.Registrarse.as_view(), name="signup"),
]


