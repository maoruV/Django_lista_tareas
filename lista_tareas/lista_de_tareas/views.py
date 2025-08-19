from django.shortcuts import render, redirect
from .models import Tarea
from django.db.models import Q

def lista_tareas(request):
    # Lógica de filtrado y búsqueda
    query = request.GET.get('q')
    categoria = request.GET.get('categoria')

    tareas = Tarea.objects.all()

    if query:
        tareas = tareas.filter(Q(titulo__icontains=query) | Q(categoria__icontains=query))

    if categoria:
        tareas = tareas.filter(categoria=categoria)

    # Lógica para crear una nueva tarea
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        if titulo:
            Tarea.objects.create(titulo=titulo, categoria=categoria)
        return redirect('lista_tareas')

    # Separar tareas pendientes y completadas (opcional)
    tareas_pendientes = tareas.filter(completada=False)
    tareas_completadas = tareas.filter(completada=True)

    context = {
        'tareas_pendientes': tareas_pendientes,
        'tareas_completadas': tareas_completadas,
        'categorias': Tarea.CATEGORIAS,
        'selected_category': categoria or '',
        'query': query or ''
    }
    return render(request, 'lista_de_tareas/lista_tareas.html', context)

def editar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    if request.method == 'POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.categoria = request.POST.get('categoria')
        tarea.save()
        return redirect('lista_tareas')
    context = {'tarea': tarea, 'categorias': Tarea.CATEGORIAS}
    return render(request, 'lista_de_tareas/editar_tarea.html', context)

def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    tarea.delete()
    return redirect('lista_tareas')

def toggle_completada(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('lista_tareas')
