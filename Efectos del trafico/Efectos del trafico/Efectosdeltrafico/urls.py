"""AccidentesTrafico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from django.contrib.auth.views import LoginView

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [

   





    #path('', LoginView.as_view()),
    path('inicio/', include('inicio.urls')),

    #pagina administrador
    path('admin/', admin.site.urls),

    #configurar logins
    path('accounts/', include('django.contrib.auth.urls')),

    #Configurar Home de la pagina
    path('home/', include('inicio.urls')),

    #Implemetar pagina de inicio de seccion
    path('paginaLogin/', include('paginaLogin.urls')),



    


    

    
    
   

    

    

   

]
