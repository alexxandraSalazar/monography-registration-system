import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

# Define la clase Monografía con sus atributos
class Monografia:
    def __init__(self, id, titulo, fecha_defensa, nota_defensa, tiempo_otorgado, tiempo_defensa, tiempo_pregunta):
        self.id = id
        self.titulo = titulo
        self.fecha_defensa = fecha_defensa
        self.nota_defensa = nota_defensa
        self.tiempo_otorgado = tiempo_otorgado
        self.tiempo_defensa = tiempo_defensa
        self.tiempo_pregunta = tiempo_pregunta

# Define la clase Estudiante con sus atributos
class Estudiante:
    def __init__(self, id, nombres, apellidos, direccion, telefono, fecha_nacimiento):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.monografia = None  # Se asignará más tarde

# Define la clase Profesor con sus atributos
class Profesor:
    def __init__(self, id, nombres, apellidos, direccion, telefono, fecha_nacimiento):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento

# Define la clase Rol para el rol de cada profesor en la monografía
class Rol:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

# Clase para relacionar a los profesores con las monografías y los roles
class ProfesorMonografia:
    def __init__(self, profesor, monografia, rol):
        self.profesor = profesor
        self.monografia = monografia
        self.rol = rol

# Listas para almacenar datos de monografías, estudiantes, profesores, roles y relaciones
monografias = []
estudiantes = []
profesores = []
roles = []
profesor_monografia = []

# Vista principal
def index(request):
    index_url = reverse('index')
    addEstuUrl = reverse('addEstu')

    # Renderiza la tabla de monografías usando HTMX en una vista parcial
    if request.htmx:
        if request.method == "GET":
            return render(request, "partials/table-mono.html", {'monos': monografias, 'index_url': index_url})

    # Renderiza la página principal o la vista de formulario de estudiantes
    if request.method == "GET":
        return render(request, 'Register/index.html', {'monos': monografias, 'index_url': index_url, 'addEstuUrl': addEstuUrl})

    return render(request, 'Register/layout.html', {'monos': monografias, 'index_url': index_url})

# Registra una nueva monografía
def registerMono(request):
    if request.method == "POST":
        try:
            # Extrae los datos de la monografía del formulario
            titulo = request.POST.get('titulo')
            fecha_defensa = request.POST.get('fecha_defensa')
            nota_defensa = int(request.POST.get('nota_defensa'))
            tiempo_otorgado = int(request.POST.get('tiempo_otorgado'))
            tiempo_defensa = int(request.POST.get('tiempo_defensa'))
            tiempo_pregunta = int(request.POST.get('tiempo_pregunta'))
                    
            # Crea y agrega la monografía a la lista
            nueva_monografia = {
                'id': len(monografias) + 1,
                'titulo': titulo,
                'fecha_defensa': fecha_defensa,
                'nota_defensa': nota_defensa,
                'tiempo_otorgado': tiempo_otorgado,
                'tiempo_defensa': tiempo_defensa,
                'tiempo_pregunta': tiempo_pregunta,
            }
            monografias.append(nueva_monografia)

            return JsonResponse({'status': 'success', 'message': 'Monografía registrada exitosamente'}, status=200)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar la Monografía'}, status=500)

    # Vista de formulario de registro para HTMX
    elif request.method == 'GET' and request.htmx:
        return render(request, "partials/register-mono.html")
    
    return render(request, 'Register/layout.html')

# Registra un nuevo estudiante
def registerEstu(request):
    if request.method == "POST":
        try:
            # Extrae datos del estudiante del formulario
            estuData = request.POST
            nombres = estuData.get('nombres')
            apellidos = estuData.get('apellidos')
            direccion = estuData.get('direccion')
            telefono = estuData.get('telefono')
            fecha_nacimiento = estuData.get('fecha_nacimiento')

            # Crea y agrega el estudiante a la lista
            nuevo_estudiante = {
                'id': len(estudiantes) + 1,
                'nombres': nombres,
                'apellidos': apellidos,
                'direccion': direccion,
                'telefono': telefono,
                'fecha_nacimiento': fecha_nacimiento,
                'monografia': None,
            }
            estudiantes.append(nuevo_estudiante)

            return JsonResponse({'status': 'success', 'message': 'Estudiante registrado exitosamente'}, status=200)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar el estudiante'}, status=500)

    # Vista de formulario de registro para HTMX
    elif request.method == "GET" and request.htmx:
        return render(request, "partials/register-estu.html")
    
    return render(request, 'Register/layout.html')

# Registra un nuevo profesor
def registerProf(request):
    if request.method == "POST":
        try:
            # Extrae datos del profesor del formulario
            estuData = request.POST
            nombres = estuData.get('nombres')
            apellidos = estuData.get('apellidos')
            direccion = estuData.get('direccion')
            telefono = estuData.get('telefono')
            fecha_nacimiento = estuData.get('fecha_nacimiento')

            # Crea y agrega el profesor a la lista
            nuevo_profesor = {
                'id': len(profesores) + 1,
                'nombres': nombres,
                'apellidos': apellidos,
                'direccion': direccion,
                'telefono': telefono,
                'fecha_nacimiento': fecha_nacimiento,
            }
            profesores.append(nuevo_profesor)

            return JsonResponse({'status': 'success', 'message': 'Profesor registrado exitosamente'}, status=200)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al registrar el Profesor'}, status=500)

    # Vista de formulario de registro para HTMX
    elif request.method == "GET" and request.htmx:
        return render(request, "partials/register-profe.html")
    
    return render(request, 'Register/layout.html')

# Vista para agregar estudiante en relación con la monografía
def addEstu(request):
    addEstuUrl = reverse('addEstu') 
    if request.htmx:
        if request.method == "POST":
            return render(request, "partials/add-estu.html", {'addEstuUrl': addEstuUrl})
        elif request.method == "GET":
            return render(request, "partials/add-estu.html", {
                'students': estudiantes, 
                'monos': monografias, 
                'addEstuUrl': addEstuUrl
            })
    return render(request, 'Register/layout.html', {'addEstuUrl': addEstuUrl})

# Función similar a addEstu para añadir un tutor a una monografía
def addTutor(request):
    addProfUrl = reverse('addTutor')
    if request.htmx:
        if request.method == "POST":
            return render(request, "partials/add-tutor.html", {'addProfUrl': addProfUrl})
        elif request.method == "GET":
            return render(request, "partials/add-tutor.html", {
                'profesores': profesores,
                'monos': monografias,
                'addProfUrl': addProfUrl
            })
    return render(request, 'Register/layout.html')

# Similar a addTutor pero para añadir jueces a una monografía
def addJudges(request):
    addProfUrl = reverse('addJudges')
    if request.htmx:
        if request.method == "POST":
            return render(request, "partials/add-judges.html", {'addProfUrl': addProfUrl})
        elif request.method == "GET":
            return render(request, "partials/add-judges.html", {
                'profesores': profesores,
                'monos': monografias,
                'addProfUrl': addProfUrl
            })
    return render(request, 'Register/layout.html')

# Eliminar una monografía
def deleteMono(request, id):
    if request.method == "POST":
        try:
            monografia = next((m for m in monografias if m['id'] == id), None)
            if monografia is not None:
                monografias.remove(monografia)
                return JsonResponse({'status': 'success', 'message': 'Monografía borrada exitosamente'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'Monografía no encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Error al borrar la Monografía'}, status=500)
    return render(request, 'Register/layout.html')

# Elimina un profesor de la lista de profesores
def deleteProf(request, id):
    if request.method == "POST":
        try:
            # Buscar el profesor por el `id` en la lista `profesores`
            profesor = next((p for p in profesores if p['id'] == id), None)
            
            # Si el profesor se encuentra, se elimina
            if profesor is not None:
                profesores.remove(profesor)
                return JsonResponse({'status': 'success', 'message': 'Profesor borrado exitosamente'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'Profesor no encontrado'}, status=404)
        
        # Si ocurre un error durante el proceso de eliminación, se captura y devuelve un mensaje de error
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar profesor: {str(e)}'}, status=500)


# Elimina un estudiante de la lista de estudiantes
def deleteEstu(request, id):
    if request.method == "POST":
        try:
            # Buscar el estudiante por el `id` en la lista `estudiantes`
            estudiante = next((e for e in estudiantes if e['id'] == id), None)
            
            # Si el estudiante se encuentra, se elimina
            if estudiante is not None:
                estudiantes.remove(estudiante)
                return JsonResponse({'status': 'success', 'message': 'Estudiante borrado exitosamente'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'Estudiante no encontrado'}, status=404)
        
        # Si ocurre un error durante el proceso de eliminación, se captura y devuelve un mensaje de error
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al eliminar estudiante: {str(e)}'}, status=500)


# Asigna un estudiante a una monografía
def AsignarEstudiante(request):
    if request.method == "POST":
        # Carga los datos enviados en la solicitud POST
        data = json.loads(request.body)
        student_id = data.get("student_id")
        mono_id = data.get("mono_id")

        try:
            # Buscar el estudiante y la monografía por sus respectivos IDs
            estudiante = next((e for e in estudiantes if e['id'] == student_id), None)
            monografia = next((m for m in monografias if m['id'] == mono_id), None)

            # Si tanto el estudiante como la monografía existen, se asignan
            if estudiante and monografia:
                estudiante['monografia'] = monografia
                return JsonResponse({"success": True, "message": "Estudiante asignado a la monografía correctamente"})
            
            # Si no se encuentra el estudiante o la monografía, se devuelve un error
            elif not estudiante:
                return JsonResponse({"success": False, "error": "Estudiante no encontrado"})
            elif not monografia:
                return JsonResponse({"success": False, "error": "Monografía no encontrada"})
        
        # Si ocurre un error durante el proceso de asignación, se captura y devuelve un mensaje de error
        except Exception as e:
            return JsonResponse({"success": False, "error": f"Error: {str(e)}"})
    
    # Si el método no es POST, se devuelve un error
    return JsonResponse({"success": False, "error": "Método no permitido"})


# Asigna un tutor a una monografía
def asignarTutor(request):
    if request.method == "POST":
        print("post asignar tutor")
        
        # Carga los datos enviados en la solicitud POST
        data = json.loads(request.body)
        profesor_id = data.get("profesor_id")
        monografia_id = data.get("monografia_id")

        try:
            # Buscar el profesor, la monografía y el rol de "Tutor"
            profesor = next((p for p in profesores if p['id'] == profesor_id), None)
            monografia = next((m for m in monografias if m['id'] == monografia_id), None)
            rol = next((r for r in roles if r['nombre'] == "Tutor"), None)

            # Si el rol "Tutor" no existe, se crea y se agrega a la lista de roles
            if not rol:
                rol = {'nombre': "Tutor"}
                roles.append(rol)

            # Si tanto el profesor como la monografía existen, se asigna el rol "Tutor" al profesor
            if profesor and monografia:
                profesor_monografia.append({
                    'profesor': profesor,
                    'monografia': monografia,
                    'rol': rol
                })
                return JsonResponse({"success": True, "message": "Tutor asignado correctamente"})
            
            # Si no se encuentra el profesor o la monografía, se devuelve un error
            elif not profesor:
                return JsonResponse({"success": False, "error": "Profesor no encontrado"})
            elif not monografia:
                return JsonResponse({"success": False, "error": "Monografía no encontrada"})
        
        # Si ocurre un error durante el proceso de asignación, se captura y devuelve un mensaje de error
        except Exception as e:
            return JsonResponse({"success": False, "error": f"Error: {str(e)}"})

    # Si el método no es POST, se devuelve un error
    return JsonResponse({"success": False, "error": "Método no permitido"})


# Asigna un jurado a una monografía
def asignarJurado(request):
    if request.method == "POST":
        print("post asignar jurado")
        
        # Carga los datos enviados en la solicitud POST
        data = json.loads(request.body)
        jurado_id = data.get("jurado_id")
        monografia_id = data.get("monografia_id")

        try:
            # Buscar el jurado, la monografía y el rol de "Jurado"
            jurado = next((p for p in profesores if p['id'] == jurado_id), None)
            monografia = next((m for m in monografias if m['id'] == monografia_id), None)
            rol = next((r for r in roles if r['nombre'] == "Jurado"), None)

            # Si el rol "Jurado" no existe, se crea y se agrega a la lista de roles
            if not rol:
                rol = {'nombre': "Jurado"}
                roles.append(rol)

            # Si tanto el jurado como la monografía existen, se asigna el rol "Jurado" al jurado
            if jurado and monografia:
                profesor_monografia.append({
                    'profesor': jurado,
                    'monografia': monografia,
                    'rol': rol
                })
                return JsonResponse({"success": True, "message": "Jurado asignado correctamente"})
            
            # Si no se encuentra el jurado o la monografía, se devuelve un error
            elif not jurado:
                return JsonResponse({"success": False, "error": "Jurado no encontrado"})
            elif not monografia:
                return JsonResponse({"success": False, "error": "Monografía no encontrada"})
        
        # Si ocurre un error durante el proceso de asignación, se captura y devuelve un mensaje de error
        except Exception as e:
            return JsonResponse({"success": False, "error": f"Error: {str(e)}"})

    # Si el método no es POST, se devuelve un error
    return JsonResponse({"success": False, "error": "Método no permitido"})
