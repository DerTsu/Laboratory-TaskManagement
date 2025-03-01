from django.contrib import admin
from django.urls import path 
from  task_app.views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tasks/', TaskList.as_view(template_name = "tasks/index.html"), name='read'),

    path('tasks/detalle/<int:pk>', TaskDetail.as_view(template_name = "tasks/details.html"), name='details'),

    path('tasks/crear', CreateTask.as_view(template_name = "tasks/create.html"), name='create'),

    path('tasks/editar/<int:pk>', UpdateTask.as_view(template_name = "tasks/update.html"), name='update'), 

    path('tasks/eliminar/<int:pk>', DeleteTask.as_view(), name='delete'),   
]
