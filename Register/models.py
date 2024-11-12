from django.db import models

# Create your models here.
from django.db import models

class Profesor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Monografia(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_defensa = models.DateField()
    nota_defensa = models.IntegerField()
    tiempo_otorgado = models.IntegerField()
    tiempo_defensa = models.IntegerField()
    tiempo_pregunta = models.IntegerField()
    def __str__(self):
        return self.titulo

class Estudiante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    monografia = models.ForeignKey(Monografia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# Esta es la tabla puente
class ProfesorMonografia(models.Model):
    monografia = models.ForeignKey(Monografia, on_delete=models.CASCADE, related_name='profesores')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profesor} - {self.rol}"