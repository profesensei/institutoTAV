from django.shortcuts import render
from .models import Alumno
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    print("hola, estoy en el index")

    context={}

    return render(request,'personas/index.html',context)

def impresoras(request):
    print("hola, estoy en impresoras")

    context={}

    return render(request,'personas/impresoras.html',context)

def mouse(request):
    print("hola, estoy en mouse")

    context={}

    return render(request,'personas/mouses.html',context)

def teclados(request):
    print("hola, estoy en teclados")

    context={}

    return render(request,'personas/teclados.html',context)

def crud_alumno(request):
    print("hola, estoy en crud_alumno")

    context={}

    return render(request,'personas/form_alumno.html',context)

def agregar_alumno(request):
    print("hola  estoy en agregar_alumno...")
    if request.method == 'POST':
        if  request.POST['opcion'] == "Grabar":
           mi_rut = request.POST['rut']
           mi_nombre= request.POST['nombre']
           mi_paterno=request.POST['aPaterno']
           mi_materno=request.POST['aMaterno']
           mi_fechaNac =request.POST['fechaNac']
           mi_genero=request.POST['genero']

           mi_foto = request.FILES['foto']

           alumno = Alumno()

           alumno.rut = mi_rut
           alumno.nombre = mi_nombre
           alumno.apellido_paterno = mi_paterno
           alumno.apellido_materno = mi_materno
           alumno.fecha_nacimiento = mi_fechaNac
           alumno.genero = mi_genero

           alumno.foto = mi_foto

           alumno.activo = 1

           alumno.save()

           return render(request, 'personas/form_alumno.html',{})
        else:
            if request.POST['opcion'] == "Editar":
                print("si, es Editar")

                #select * from alumno
                alumno= Alumno.objects.all()
                #alumno = Alumno.objects.filter(activo = 1)
                #alumno = Alumno.objects.filter(activo=1, genero='femenino')
                context = { 'alumno':alumno }

                return render(request, 'personas/editar_alumnos.html', context)

    else:
        print("Error, no es un POST")


def form_editar(request, pk):

    print("Hola, estoy en form_editar y la pk es "+ str(pk) )

    alumno = Alumno.objects.get(id_alumno = pk)

    context = { 'alumno':alumno }

    return render(request, 'personas/form_editar.html', context )


def form_eliminar(request, pk):

    print("Hola, estoy en form_eliminar y la pk es "+ str(pk) )

    alumno = Alumno.objects.get(id_alumno = pk)

    #alumno.delete()

    #alumnos = Alumno.objects.all()

    context = {'alumno': alumno }

    return render(request, 'personas/form_eliminar.html', context )


def actualizar(request):
    print("hola  estoy en actualizar...")
    if request.method == 'POST':
        if  request.POST['opcion'] == "Actualizar":
           mi_id_alumno = request.POST['id_alumno']

           alumnoOld = Alumno.objects.get(id_alumno = mi_id_alumno)

           mi_rut = request.POST['rut']
           mi_nombre= request.POST['nombre']
           mi_paterno=request.POST['aPaterno']
           mi_materno=request.POST['aMaterno']
           mi_fechaNac =request.POST['fechaNac']
           mi_genero=request.POST['genero']

           try:
               if request.FILES['foto']:
                   mi_foto = request.FILES['foto']
           except:
               print("Entró a else de foto")
               mi_foto = alumnoOld.foto

           alumno = Alumno()
           alumno.id_alumno = mi_id_alumno
           alumno.rut = mi_rut
           alumno.nombre = mi_nombre
           alumno.apellido_paterno = mi_paterno
           alumno.apellido_materno = mi_materno
           alumno.fecha_nacimiento = mi_fechaNac
           alumno.genero = mi_genero

           if mi_foto is not None:
               alumno.foto = mi_foto
           else:
               alumno.foto = ""

           alumno.activo = 1

           alumno.save()

           # select * from alumno
           alumnos = Alumno.objects.all()

           context = {'alumno': alumnos}

           return render(request, 'personas/editar_alumnos.html', context)
        else:
            if request.POST['opcion'] == "Cancelar":
                print("si, es Cancelar")

                #select * from alumno
                alumnos= Alumno.objects.all()

                context = { 'alumno':alumnos }

                return render(request, 'personas/editar_alumnos.html', context)

    else:
        print("Error, no es un POST")


def eliminar(request):
    print("hola  estoy en eliminarr...")
    if request.method == 'POST':
        if  request.POST['opcion'] == "Eliminar":

           mi_id_alumno = request.POST['id_alumno']

           alumno = Alumno.objects.get(id_alumno = mi_id_alumno)

           alumno.delete()

           alumnos = Alumno.objects.all()

           context = {'alumno': alumnos}

           return render(request, 'personas/editar_alumnos.html', context)
        else:
            if request.POST['opcion'] == "Cancelar":
                print("si, es Cancelar")

                #select * from alumno
                alumnos= Alumno.objects.all()

                context = { 'alumno':alumnos }

                return render(request, 'personas/editar_alumnos.html', context)

    else:
        print("Error, no es un POST")
