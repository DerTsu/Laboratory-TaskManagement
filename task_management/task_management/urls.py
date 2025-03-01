from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path 
from  task_app.views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [

    path('admin/', admin.site.urls),

    path('arepas/', TaskList.as_view(template_name = "tasks/index.html"), name='read'),

    path('arepas/detalle/<int:pk>', TaskDetail.as_view(template_name = "tasks/details.html"), name='details'),

    path('arepas/crear', CreateTask.as_view(template_name = "tasks/create.html"), name='create'),

    path('arepas/editar/<int:pk>', UpdateTask.as_view(template_name = "tasks/update.html"), name='update'), 

    path('arepas/eliminar/<int:pk>', DeleteTask.as_view(), name='delete'),   
]
