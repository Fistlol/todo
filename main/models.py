from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    title = models.CharField(max_length=100)


class Todo(models.Model):
    task = models.CharField(max_length=100)
    created = models.DateTimeField(default=None, null=True, blank=True)
    due_on = models.DateTimeField(default=None, null=True, blank=True)
    owner = models.CharField(max_length=100)
    mark = models.BooleanField(default=True)
    img = models.ImageField(upload_to='images',null=True, blank=True)  # stores uploaded image
    file = models.FileField(upload_to='files',null=True, blank=True)
    list_id = models.ForeignKey(TodoList, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ('task',)


# from django.db import models


# class ToDoList(models.Model):
#     title = models.CharField(max_length=100, null=False, blank=False)

#     class Meta:
#         verbose_name = 'Список задач'
#         verbose_name_plural = 'Списки задач'

#     def __str__(self) -> str:
#         return self.title


# class Task(models.Model):
#     title = models.CharField(max_length=100, null=False, blank=False)
#     created = models.DateField(auto_now=True)
#     due_on = models.DateField(null=True, blank=True)
#     owner = models.CharField(max_length=100, null=True, blank=True)
#     completed = models.BooleanField(default=False, null=False, blank=False)
#     todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, null=False, blank=False, related_name='tasks')

#     class Meta:
#         verbose_name = 'Задача'
#         verbose_name_plural = 'Задачи'

#     def __str__(self) -> str:
#         return self.title
