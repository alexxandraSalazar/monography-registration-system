from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register-estu/', views.registerEstu, name='registerEstu'),
    path('register-Prof/', views.registerProf, name='registerProf'),
    path('register-mono/', views.registerMono, name='registerMono'),
    path('add-estu/', views.addEstu, name='addEstu'),
    path('add-tutor/', views.addTutor, name='addTutor'),
    path('add-judges/', views.addJudges, name='addJudges'),
    path('delete-mono/<int:id>', views.deleteMono, name='deleteMono'),
    path('delete-Estu/<int:id>', views.deleteEstu, name='deleteEstu'),
    path('delete-Prof/<int:id>', views.deleteProf, name='deleteProf'),
    path('asignar-estudiante', views.AsignarEstudiante, name="asignarEstudiante"),
    path('asignar-tutor', views.AsignarTutor, name="asignarTutor"),

]
