from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = 'New', 'Новая'
    IN_PROGRESS = 'In Progress', 'В процессе'
    DONE = 'Done', 'Выполнена'


class ToDoList(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name="Описание"
    )
    status = models.CharField(
        max_length=20,
        verbose_name="Статус",
        choices=StatusChoice.choices,
        default=StatusChoice.NEW
    )
    due_date = models.DateTimeField(
        verbose_name="Срок выполнения",
        blank=False, null=True
    )

    def __str__(self):
        return f'{self.title} - {self.description}'
