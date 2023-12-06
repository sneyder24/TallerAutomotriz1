from django.shortcuts import render, redirect
from mantenimiento.models import Cita
from mantenimiento.forms import CitaForm,CitaUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

   
@login_required 
def cita_crear(request):
    titulo="Cita"
    if request.method== 'POST':
        form= CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'La Cita se creo correctamente.')
            return redirect('citas')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= CitaForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"mantenimiento/citas/crear.html", context)

@login_required
def cita_listar(request):
    titulo="Citas"
    modulo ="Mantenimiento"
    cita= Cita.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "citas":cita
    }
    return render(request,"mantenimiento/citas/listar.html", context)

@login_required
def cita_modificar(request,pk):
    titulo="Cita"
    cita= Cita.objects.get(id=pk)
    if request.method== 'POST':
        form= CitaUpdateForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se modifico correctamente.')
            return redirect('citas')
        
    else:
        form= CitaUpdateForm(instance=cita)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"mantenimiento/citas/modificar.html", context)

@login_required
def cita_eliminar(request,pk):
    cita= Cita.objects.filter(id=pk)
    cita.delete()
    cita.update(estado="0")
    return redirect('citas')