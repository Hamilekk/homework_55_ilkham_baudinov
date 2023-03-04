from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import ToDoForm
from webapp.models import ToDoList


def detail_view(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    context = {
        'task': task
    }
    return render(request, 'task.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = ToDoForm()
        return render(request, 'add_task.html', context={
            'form': form
        })

    form = ToDoForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request, 'add_task.html', context={
            'form': form
        })
    else:
        task = ToDoList.objects.create(**form.cleaned_data)
        return redirect('task_detail', pk=task.pk)


def edit_task(request: WSGIRequest, pk):
    task = get_object_or_404(ToDoList, pk=pk)

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, 'edit_task.html', context={'form': form, 'task': task})

    form = ToDoForm(instance=task)
    return render(request, 'edit_task.html', context={'form': form, 'task': task})


def delete_task(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'delete_task.html', {'task': task})


def delete_task_confirm(request, pk):
    guest = get_object_or_404(ToDoList, pk=pk)
    guest.delete()
    return redirect(reverse('index'))


def task_list(request):
    tasks = ToDoList.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list_delete.html', context)


def delete_selected_tasks(request):
    if request.method == 'POST':
        tasks_to_delete = request.POST.getlist('tasks_to_delete')
        ToDoList.objects.filter(pk__in=tasks_to_delete).delete()
    return redirect('task_list')
