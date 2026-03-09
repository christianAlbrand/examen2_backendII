from django.shortcuts import render, redirect
from decimal import Decimal
from .models import Auto

def agregar_auto(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        anio = int(request.POST['año'])
        precio = Decimal(request.POST['precio'])

        Auto.objects.create(
            marca=marca,
            modelo=modelo,
            año=anio,
            precio=precio
        )

        return redirect('listar_autos')

    return render(request, 'autos_app/agregar_auto.html')

def listar_autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos_app/listar_autos.html', {'autos': autos})

def home(request):
    return render(request, 'autos_app/home.html')