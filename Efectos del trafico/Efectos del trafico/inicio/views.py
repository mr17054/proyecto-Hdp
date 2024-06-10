from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
#from AccidentesTrafico.forms import myUserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.

def home(request):
    #render de la pagina html home de la pagina de inicio
    return render(request,"inicio/home.html")


class Registrarse(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


