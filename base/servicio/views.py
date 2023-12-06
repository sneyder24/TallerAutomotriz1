from django.shortcuts import render, redirect
from servicio.models import Servicio,Detalle_servicio
from servicio.forms import ServicioForm,ServicioUpdateForm,Detalle_servicioForm, Detalle_servicioUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def servicio_crear(request):
    titulo="Servicio"
    if request.method=='POST':
        form=ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El Servicio se ha creado correctamente.')
            return redirect('servicios')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= ServicioForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"servicio/servicio/crear.html", context)

@login_required
def servicio_listar(request):
    titulo="Servicio"
    modulo ="Servicio"
    servicio= Servicio.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "servicios":servicio
    }
    return render(request,"servicio/servicio/listar.html", context)

@login_required
def servicio_modificar(request,pk):
    titulo="Servicio"
    servicio= Servicio.objects.get(id=pk)
    
    if request.method== 'POST':
        form= ServicioUpdateForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('servicios')
    else:
        form= ServicioUpdateForm(instance=servicio)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"servicio/servicio/modificar.html", context)

@login_required
def servicio_eliminar(request,pk):
    servicio= Servicio.objects.filter(id=pk)
    servicio.delete()
    servicio.update()
    return redirect('servicios')
   
@login_required 
def detalleservicio_crear(request):
    titulo="Detalle_servicio"
    if request.method== 'POST':
        form= Detalle_servicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El Detalle del servicio se ha creado correctamente.')
            return redirect('detalleservicios')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= Detalle_servicioForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"servicio/detalleservicio/crear.html", context)

@login_required
def detalleservicio_listar(request):
    titulo="Detalle_servicio"
    modulo ="Servicio"
    detalle_servicio= Detalle_servicio.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "detalleservicios":detalle_servicio
    }
    return render(request,"servicio/detalleservicio/listar.html", context)

@login_required
def detalleservicio_modificar(request,pk):
    titulo="Detalle_servicios"
    detalle_servicio= Detalle_servicio.objects.get(id=pk)
    if request.method== 'POST':
        form= Detalle_servicioUpdateForm(request.POST, instance=detalle_servicio)
        if form.is_valid():
            form.save()
            return redirect('detalleservicios')
    else:
        form= Detalle_servicioUpdateForm(instance=detalle_servicio)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"servicio/detalleservicio/modificar.html", context)

@login_required
def detalleservicio_eliminar(request,pk):
    detalle_servicio= Detalle_servicio.objects.filter(id=pk)
    detalle_servicio.delete()
    detalle_servicio.update()
    return redirect('detalleservicios') 

 

def ultimoservicio(request):
    ultimo_servicio = Servicio.objects.filter(estado='1').order_by('-fecha_creacion').first()

    return render(request, 'index.html', {
        'ultimo_servicio': ultimo_servicio,
    })