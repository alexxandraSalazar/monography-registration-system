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
]
