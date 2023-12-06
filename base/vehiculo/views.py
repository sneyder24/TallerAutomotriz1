from django.shortcuts import render, redirect
from vehiculo.models import Vehiculo
from vehiculo.models import Linea
from vehiculo.forms import VehiculoForm, VehiculoUpdateForm, LineaForm, LineaUpdateForm
from django.contrib import messages

# Create your views here.

def vehiculo_crear(request):
    titulo="Vehiculo" 
    if request.method == 'POST':
        form=VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request ,'El Vehiculo Se Creo Correctamente')
            return redirect('vehiculos')
        else:
            messages.error(request,'El Vehiculo No Se Creo Correctamente')
    else:
        form =VehiculoForm
    context={
        "titulo": titulo,
        "form": form,
    }
    return render(request,"vehiculo/vehiculo/crear.html", context)

def vehiculo_listar(request):
    titulo="Vehiculo" 
    modulo="Vehiculo"
    vehiculo = Vehiculo.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "vehiculos":vehiculo
    }
    return render(request,"vehiculo/vehiculo/listar.html", context)

def vehiculo_modificar(request,pk):
    titulo=" Vehiculo"
    vehiculo= Vehiculo.objects.get(id=pk)
    if request.method == 'POST':
        form= VehiculoUpdateForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request ,'El Vehiculo Se Modifico Correctamente')
            return redirect('vehiculos')
    else:
        form= VehiculoUpdateForm(instance= vehiculo)
    context={
        "titulo": titulo,
        "form": form
    }
    return render(request, "vehiculo/vehiculo/modificar.html", context)

def vehiculo_eliminar(request,pk):
    vehiculo=Vehiculo.objects.filter(id=pk)
    vehiculo.delete()
    vehiculo.update()
    return redirect('vehiculos')

def linea_crear(request):
    titulo ="Linea"
    if request.method== 'POST':
        form = LineaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request ,'La Linea Se Creo Correctamente')
            return redirect('lineas')
        else:
            messages.error(request,'La Linea No Se Creo Correctamente')
    else:
        form= LineaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"vehiculo/linea/crear.html", context)

def linea_listar(request):
    titulo ="Linea"
    modulo ="Vehiculo"
    linea= Linea.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "lineas":linea
    }
    return render(request,"vehiculo/linea/listar.html", context)

def linea_modificar(request, pk):
    titulo= "Linea" #titulo del boton
    linea=Linea.objects.get(id=pk)
    if request.method == 'POST':
        form= LineaUpdateForm(request.POST, instance= linea)
        if form.is_valid():
            form.save()
            messages.success(request ,'La Linea Se Modifico Correctamente')
            return redirect('lineas')
    else:
        form=LineaUpdateForm(instance= linea)
    context={
        "titulo": titulo,
        "form": form
    }
    return render(request, "vehiculo/linea/modificar.html",context)

def linea_eliminar(request,pk):
    linea= Linea.objects.filter(id=pk)
    linea.delete()
    linea.update(estado="0")
    return redirect('lineas')
