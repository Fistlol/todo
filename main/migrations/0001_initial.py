# Generated by Django 4.0.3 on 2022-03-12 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Список задач',
                'verbose_name_plural': 'Списки задач',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now=True)),
                ('due_on', models.DateField(blank=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=100, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.todolist')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
