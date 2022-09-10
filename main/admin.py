from django.contrib import admin
from .models import TodoList, Todo

@admin.register(Todo)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('task', 'created', 'due_on', 'owner', 'mark','list_id','img','file')
    search_fields = ('task', 'mark','list_id')
    list_filter = ('task', 'created', 'due_on', 'owner', 'mark','list_id',)

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


# from django.contrib import admin
# from .models import ToDoList, Task

# @admin.register(ToDoList)
# class ToDoListAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     empty_value_display = '- empty -'
#     search_fields = ('title',)


# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'created', 'due_on', 'owner', 'completed', 'todo_list')
#     empty_value_display = '- empty -'
#     list_filter = ('completed', 'todo_list', 'owner')
#     search_fields = ('title', 'completed')