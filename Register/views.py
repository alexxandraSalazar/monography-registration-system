import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Monografia, Estudiante, Profesor, Rol, ProfesorMonografia



# Create your views here.
def index(request):
    index_url = reverse('index')
    addEstuUrl = reverse('addEstu')
    monos = Monografia.objects.all()

    if request.htmx:
        if request.method == "GET":
            return render(request, "partials/table-mono.html", {'monos': monos, 'index_url': index_url})
    
    if request.method == "GET":
        return render(request, 'Register/index.html', {'monos': monos, 'index_url': index_url, 'addEstuUrl': addEstuUrl})

    return render(request, 'Register/layout.html', {'monos': monos, 'index_url': index_url})


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
        addEstuUrl = reverse('addEstu') 
        if request.htmx:
            if request.method == "POST":
                print('post')
                return render(request, "partials/add-estu.html", {'addEstuUrl': addEstuUrl})
            elif request.method == "GET":
                monos = Monografia.objects.all()
                students = Estudiante.objects.all()
                return render(request, "partials/add-estu.html",{'students': students, 'monos': monos, 'addEstuUrl': addEstuUrl})
        return render(request,'Register/layout.html', {'addEstuUrl': addEstuUrl})
    
def addTutor(request):
        addProfUrl = reverse('addTutor')
        if request.htmx:
            if request.method == "POST":
                return render(request, "partials/add-tutor.html", {'addProfUrl': addProfUrl})
            elif request.method == "GET":
                monos = Monografia.objects.all()
                profesores = Profesor.objects.all()
                return render(request, "partials/add-tutor.html",{'profesores': profesores,'monos': monos, 'addProfUrl': addProfUrl})
        return render(request,'Register/layout.html')
    
def addJudges(request):
        addProfUrl = reverse('addJudges')
        if request.htmx:
            if request.method == "POST":
                return render(request, "partials/add-judges.html", {'addProfUrl': addProfUrl})
            elif request.method == "GET":
                profesores = Profesor.objects.all()
                return render(request, "partials/add-judges.html",{'profesores': profesores, 'addProfUrl': addProfUrl})
        return render(request,'Register/layout.html')
    
    
def deleteMono(request, id):
    if request.method == "POST":
        print('POST request received')
        try:
            monografia = Monografia.objects.get(id=id) 
            monografia.delete() 
            return JsonResponse({'status': 'success', 'message': 'Monografía borrada exitosamente'}, status=200)
            
        except Monografia.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Monografía no encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar Monografía: {str(e)}'}, status=500) 

def deleteProf(request, id):
    if request.method == "POST":
        try:
            profesor = Profesor.objects.get(id=id)
            profesor.delete()
            return JsonResponse({'status': 'success', 'message': 'Profesor borrado exitosamente'}, status=200)   
        except Profesor.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Profesor no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar profesor: {str(e)}'}, status=500)

def deleteEstu(request, id):
    if request.method == "POST":
        try:
            estudiante = Estudiante.objects.get(id=id)
            estudiante.delete()
            return JsonResponse({'status': 'success', 'message': 'Estudiante borrado exitosamente'}, status=200)   
        except Estudiante.DoesNotExist: 
            return JsonResponse({'status': 'error', 'message': 'Estudiante no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar estudiante: {str(e)}'}, status=500)
        
        
def AsignarEstudiante(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student_id = data.get("student_id")
        mono_id = data.get("mono_id")

        try:
            estudiante = Estudiante.objects.get(id=student_id)
            monografia = Monografia.objects.get(id=mono_id)
            
            estudiante.monografia = monografia
            estudiante.save()  

            return JsonResponse({"success": True})
        except Estudiante.DoesNotExist:
            return JsonResponse({"success": False, "error": "Estudiante no encontrado"})
        except Monografia.DoesNotExist:
            return JsonResponse({"success": False, "error": "Monografía no encontrada"})
    return JsonResponse({"success": False, "error": "Método no permitido"})


def AsignarTutor(request):
    if request.method == "POST":
        data = json.loads(request.body)
        profesor_id = data.get("profesor_id")
        monografia_id = data.get("monografia_id")

        try:
            profesor = Profesor.objects.get(id=profesor_id)
            monografia = Monografia.objects.get(id=monografia_id)
            rol, created = Rol.objects.get_or_create(nombre="Tutor")

            ProfesorMonografia.objects.create(profesor=profesor, monografia=monografia, rol=rol)

            return JsonResponse({"success": True, "message": "Tutor asignado correctamente"})
        except Profesor.DoesNotExist:
            return JsonResponse({"success": False, "error": "Profesor no encontrado"})
        except Monografia.DoesNotExist:
            return JsonResponse({"success": False, "error": "Monografía no encontrada"})
    return JsonResponse({"success": False, "error": "Método no permitido"})