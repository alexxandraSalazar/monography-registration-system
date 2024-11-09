from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Monografia, Estudiante, Profesor, Rol, ProfesorMonografia
import sweetify

# Create your views here.
def index(request):
        if request.htmx:
            if request.method == "GET":
                monos = Monografia.objects.all()
                return render(request, "partials/table-mono.html", {'monos' : monos})
        monos = Monografia.objects.all()
        return render(request,'Register/layout.html', {'monos' : monos})

def registerMono(request):
    if request.method == "POST":
        try:
            titulo = request.POST.get('titulo')
            fecha_defensa = request.POST.get('fecha_defensa')
            nota_defensa = request.POST.get('nota_defensa')
            tiempo_otorgado = request.POST.get('tiempo_otorgado')
            tiempo_defensa = request.POST.get('tiempo_defensa')
            tiempo_pregunta = request.POST.get('tiempo_pregunta')
                    
            Monografia.objects.create(
                titulo = titulo,
                fecha_defensa = fecha_defensa,
                nota_defensa = nota_defensa,
                tiempo_otorgado = tiempo_otorgado,
                tiempo_defensa = tiempo_defensa,
                tiempo_pregunta = tiempo_pregunta
            )
        
            return JsonResponse({'status': 'success', 'message': 'Monografía registrada exitosamente'}, status=200)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar la Monografía'}, status=500)
        
    elif request.method == 'GET' and request.htmx:
        return render(request, "partials/register-mono.html")
    return render(request,'Register/layout.html')

def registerEstu(request):
    if request.method == "POST":
        try:
            estuData = request.POST
            nombres = estuData.get('nombres')
            apellidos = estuData.get('apellidos')
            direccion = estuData.get('direccion')
            telefono = estuData.get('telefono')
            fecha_nacimiento = estuData.get('fecha_nacimiento')
            
            Estudiante.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                direccion=direccion,
                telefono=telefono,
                fecha_nacimiento=fecha_nacimiento
            )
            
            return JsonResponse({'status': 'success', 'message': 'Estudiante registrado exitosamente'}, status=200)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar el estudiante'}, status=500)

    elif request.method == "GET" and request.htmx:
        return render(request, "partials/register-estu.html")
    
    return render(request, 'Register/layout.html')


def registerProf(request):
    if request.method == "POST":
        try:
            estuData = request.POST
            nombres = estuData.get('nombres')
            apellidos = estuData.get('apellidos')
            direccion = estuData.get('direccion')
            telefono = estuData.get('telefono')
            fecha_nacimiento = estuData.get('fecha_nacimiento')
            
            Profesor.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                direccion=direccion,
                telefono=telefono,
                fecha_nacimiento=fecha_nacimiento
            )
            
            return JsonResponse({'status': 'success', 'message': 'Profesor registrado exitosamente'}, status=200)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar el Profesor'}, status=500)

    elif request.method == "GET" and request.htmx:
        print('get')
        return render(request, "partials/register-profe.html")
    return render(request,'Register/layout.html')
    
def addEstu(request):
        if request.htmx:
            if request.method == "POST":
                print('post')
                
                return render(request, "partials/add-estu.html")
            elif request.method == "GET":
                monos = Monografia.objects.all()
                students = Estudiante.objects.all()
                return render(request, "partials/add-estu.html",{'students': students, 'monos': monos})
        return render(request,'Register/layout.html')
    
def addTutor(request):
        if request.htmx:
            if request.method == "POST":
                return render(request, "partials/add-tutor.html")
            elif request.method == "GET":
                profesores = Profesor.objects.all()
                return render(request, "partials/add-tutor.html",{'profesores': profesores})
        return render(request,'Register/layout.html')
    
def addJudges(request):
        if request.htmx:
            if request.method == "POST":
                return render(request, "partials/add-judges.html")
            elif request.method == "GET":
                profesores = Profesor.objects.all()
                return render(request, "partials/add-judges.html",{'profesores': profesores})
        return render(request,'Register/layout.html')
    
    
def deleteMono(request, id):
    if request.htmx:
        if request.method == "POST":
            monografia = Monografia.objects.get(id=id)
            monografia.delete()
            msg = "Monografía eliminada con éxito"
            monos = Monografia.objects.all()  
            return render(request, "partials/table-mono.html", {'monos': monos})
        

def deleteProf(request, id):
    if request.htmx:
        if request.method == "POST":
            profesor = Profesor.objects.get(id=id)
            profesor.delete()
            msg = "Profesor eliminado con éxito"
            profesores = Profesor.objects.all()  
            return render(request, "partials/table-mono.html",{'profesores': profesores})
        
def deleteEstu(request, id):
    if request.htmx:
        if request.method == "POST":
            estudiante = Estudiante.objects.get(id=id)
            estudiante.delete()
            msg = "Estudiante eliminada con éxito"
            students = Estudiante.objects.all()  
            return render(request, "partials/table-mono.html",{'students': students})

