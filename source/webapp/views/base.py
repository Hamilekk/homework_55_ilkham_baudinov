from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import ToDoList


def index_view(request: WSGIRequest):
    task_list = ToDoList.objects.all()
    context = {
        'tasks': task_list
    }
    return render(request, 'index.html', context=context)
