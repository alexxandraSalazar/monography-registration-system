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
    path('asignar-tutor', views.asignarTutor, name="asignarTutor"),
    path('asignar-Jurado', views.asignarJurado, name="asignarJurado"),
    path('edit_monografia/<int:id>/', views.editMono, name='editMono'),
    path('monografia/data/<int:pk>/', views.pdfdata, name='pdfdata'),
    path('monografia/<int:id>/details/', views.get_monografia_details, name='monografia_details'),
    path('monografia/<int:id>/update/', views.update_monografia, name='update_monografia'),
]   
