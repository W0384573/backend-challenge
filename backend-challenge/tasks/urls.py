from django.urls import path
from .views import task_list, create_task, update_task, delete_task

urlpatterns = [
    path('', task_list, name='task-list'),
    path('create/', create_task, name='task-create'),
    path('<int:pk>/update/', update_task, name='task-update'),
    path('<int:pk>/delete/', delete_task, name='task-delete'),
]
