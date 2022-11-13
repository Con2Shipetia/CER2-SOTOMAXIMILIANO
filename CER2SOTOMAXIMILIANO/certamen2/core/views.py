from django.shortcuts import render
from core.models import Correspondencia

# Create your views here.

def home(request):
    correspondencia = Correspondencia.objects.all()
    lista = {'correspondencia': correspondencia}

    return render(request, "core/index.html", lista)
