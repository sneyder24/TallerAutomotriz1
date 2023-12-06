from django.shortcuts import render,redirect
from inventario.models import Repuesto
from inventario.models import Marcarepuesto
from inventario.forms import  RepuestoForm,RepuestoUpdateForm,MarcarepuestoForm,MarcarepuestoUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
@login_required
def repuesto_crear(request):
    titulo="Repuesto"
    if request.method== 'POST':
        form= RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El repuesto se creo correctamente.')
            return redirect('repuestos')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= RepuestoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventario/repuestos/crear.html", context)

@login_required
def repuesto_listar(request):
    titulo="Repuestos"
    modulo ="Inventario"
    repuesto=Repuesto.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "repuestos":repuesto
    }
    return render(request,"inventario/repuestos/listar.html", context)

@login_required
def repuesto_modificar(request,pk):
    titulo="Repuesto"
    repuesto=Repuesto.objects.get(id=pk)
    if request.method== 'POST':
        form= RepuestoUpdateForm(request.POST, instance= repuesto)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('repuestos')
    else:
        form=  RepuestoUpdateForm(instance= repuesto)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventario/repuestos/modificar.html", context)

@login_required
def repuesto_eliminar(request,pk):
    repuesto=Repuesto.objects.filter(id=pk)
    repuesto.delete()
    repuesto.update()
    return redirect('repuestos')



 
@login_required
def marcarepuesto_crear(request):
    titulo="Marcarepuesto"
    
    if request.method== 'POST':
        form= MarcarepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'La marca del repuesto se creo correctamente.')
            return redirect('marcarepuestos')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= MarcarepuestoForm()
    context={
        "titulo":titulo,
        
        "form":form
        }
    return render(request,"inventario/marcarepuesto/crear.html", context)

@login_required
def marcarepuesto_listar(request):
    titulo="Marcarepuesto"
    modulo="Inventario"
    marcarepuesto= Marcarepuesto.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "marcarepuestos":marcarepuesto
    }
    return render(request,"inventario/marcarepuesto/listar.html", context)

@login_required
def marcarepuesto_modificar(request,pk):
    titulo="Marcarepuesto"
    marcarepuesto= Marcarepuesto.objects.get(id=pk)
    if request.method== 'POST':
        form= MarcarepuestoUpdateForm(request.POST, instance=marcarepuesto)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se modifico correctamente.')
            return redirect('marcarepuestos')
    else:
        form= MarcarepuestoUpdateForm(instance=marcarepuesto)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventario/marcarepuesto/modificar.html", context)

@login_required
def marcarepuesto_eliminar(request,pk):
    marcarepuesto= Marcarepuesto.objects.filter(id=pk)
    marcarepuesto.delete()
    marcarepuesto.update()
    return redirect('marcarepuestos')




 

