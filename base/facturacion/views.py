from django.shortcuts import render, redirect
from facturacion.models import Venta
from facturacion.forms import VentaForm, VentaUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def venta_crear(request):
    titulo="Venta"
    if request.method== 'POST':
        form= VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'La venta se creo correctamente')
            return redirect('ventas')
        else:
            messages.error(request,'El formulario tiene errores.')
    else:
        form=VentaForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"facturacion/venta/crear.html", context)
@login_required
def venta_listar(request):
    titulo="Venta"
    modulo ="Facturacion"
    venta= Venta.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "ventas":venta
    }
    return render(request,"facturacion/venta/listar.html",context)

@login_required
def venta_modificar(request,pk):
    titulo="Venta"
    venta= Venta.objects.get(id=pk)
    if request.method == 'POST':
        form= VentaUpdateForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'la venta se modifico correctamente')
            return redirect('ventas')
    else:
        form=VentaUpdateForm(instance=venta)
    context={
        "titulo": titulo,
        "form": form
        }
    return render(request, "facturacion/venta/modificar.html",context)

@login_required
def venta_eliminar(request,pk):
    venta=Venta.objects.filter(id=pk)
    venta.delete()
    venta.update()
    return redirect('ventas')
