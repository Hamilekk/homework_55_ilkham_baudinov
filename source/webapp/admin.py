from django.contrib import admin

from webapp.models import ToDoList


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'due_date')
    list_filter = ('id', 'title', 'description', 'status', 'due_date')
    search_fields = ('id', 'title', 'status', 'due_date')
    fields = ('id', 'title', 'description', 'status', 'due_date')
    readonly_fields = ('id', 'title', 'description', 'status', 'due_date')


admin.site.register(ToDoList, ToDoAdmin)
