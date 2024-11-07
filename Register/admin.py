from django.contrib import admin
from .models import Profesor, Estudiante, Rol, Monografia, ProfesorMonografia
# Register your models here.

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Rol)
admin.site.register(Monografia)
admin.site.register(ProfesorMonografia)

