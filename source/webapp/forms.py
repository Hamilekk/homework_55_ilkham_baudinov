from django import forms
from django.core.validators import MinLengthValidator,RegexValidator

from webapp.models import ToDoList, StatusChoice


class ToDoForm(forms.ModelForm):
    title = forms.CharField(
        validators=(MinLengthValidator(limit_value=2, message='Заголовок не может быть короче 2-ух символов'),))
    class Meta:
        model = ToDoList
        fields = ('title', 'description', 'status', 'due_date')
        labels = {
            'title': 'Заголовок задачи',
            'description': 'Описание задачи',
            'status': 'Статус',
            'due_date': 'Срок выполнения'
        }

