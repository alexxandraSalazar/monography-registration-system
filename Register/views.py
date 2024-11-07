from django.shortcuts import render
from .models import Monografia, Estudiante, Profesor, Rol, ProfesorMonografia
# Create your views here.
def index(request):
        if request.htmx:
            monos = Monografia.objects.all()
            return render(request, "partials/table-mono.html", {'monos' : monos})
        return render(request,'Register/layout.html')

def registerMono(request):
        if request.htmx:
            return render(request, "partials/register-mono.html")
        return render(request,'Register/layout.html')

def registerEstu(request):
        if request.htmx:
            return render(request, "partials/register-estu.html")
        return render(request,'Register/layout.html')

def registerProf(request):
        if request.htmx:
            return render(request, "partials/register-profe.html")
        return render(request,'Register/layout.html')
    
def addEstu(request):
        if request.htmx:
            return render(request, "partials/add-estu.html")
        return render(request,'Register/layout.html')
    
def addTutor(request):
        if request.htmx:
            return render(request, "partials/add-tutor.html")
        return render(request,'Register/layout.html')
    
def addJudges(request):
        if request.htmx:
            return render(request, "partials/add-judges.html")
        return render(request,'Register/layout.html')

