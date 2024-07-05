from django.urls import path

# from . import views

from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView

app_name = 'todo'
urlpatterns = [
    path('todo/', TaskListView.as_view(), name='view-tasks'),
    path('tasks/new/', TaskCreateView.as_view(), name='create-task'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='update-task'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='delete-task'),
    ]
