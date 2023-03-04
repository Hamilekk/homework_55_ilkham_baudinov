from django.urls import path

from webapp.views.base import index_view
from webapp.views.task import add_view, detail_view, edit_task, delete_task, delete_task_confirm, task_list, \
    delete_selected_tasks

urlpatterns = [
    path('', index_view, name='index'),
    path('task/add/', add_view, name='task_add'),
    path('task/<int:pk>/', detail_view, name='task_detail'),
    path('task/edit/<int:pk>/', edit_task, name='task_edit'),
    path('task/delete/<int:pk>/', delete_task, name='task_delete'),
    path('task/delete_confirm/<int:pk>/', delete_task_confirm, name='task_delete_confirm'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/delete_selected/', delete_selected_tasks, name='delete_selected_tasks'),
]
