from django.shortcuts import redirect, render
from usuarios.models import Usuario,Arl
from inventario.models import Repuesto,Marcarepuesto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def principaliniciado(request):
    titulo="Bienvenido Al Sistema"
    usuario=Usuario.objects.all().count()
    arl=Arl.objects.all().count()
    repuesto=Repuesto.objects.all().count()
    marcarepuesto= Marcarepuesto.objects.all().count()
    context={
        "usuarios":usuario,
        "arls":arl,
        "repuestos":repuesto,
        "marcarepuestos":marcarepuesto,
 
        "titulo":titulo
    }
    
    return render(request, "index.html",context)



def principal(request):
    return render(request, 'homepage/index.html')

def services_view(request):
    return render(request, 'homepage/services.html')
def us_view(request):
    return render(request, 'homepage/us.html')

def contacme_view(request):
    return render(request, 'homepage/contactme.html')

def Manualdeayudaclientes_view(request):
    return render(request, 'static/doc/Manualdeayudaclientes.pdf')

def TérminosyCondiciones_view(request):
    return render(request, 'static/doc/Terminosycondiciones.pdf')

def Manualdeayudalogin_view(request):
    return render(request, 'static/doc/Manualdeayudalogin.pdf')

def logout_user(request):
    logout(request)
    return redirect('login')

def login_view(request):
    return render(request, 'registration/login.html')