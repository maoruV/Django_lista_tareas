from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('toggle/<int:tarea_id>/', views.toggle_completada, name='toggle_completada'),
]