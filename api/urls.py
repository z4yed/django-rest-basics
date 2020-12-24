from django.urls import path
from . import views

urlpatterns = [
    # path('', views.api_overview, name='overview'),
    # path('task-list/', views.todo_list, name='todo-list'),
    # path('task-detail/<task_id>/', views.todo_details, name='todo-detail'),
    # path('task-create/', views.create_todo, name='create-todo'),
    # path('task-update/<task_id>/', views.update_todo, name='update-todo'),
    # path('task-delete/<task_id>/', views.delete_todo, name='delete-todo'),

    path('', views.ApiOverview.as_view(), name='overview'),
    path('task-list/', views.TaskList.as_view(), name='todo-list'),
    path('task-details/<task_id>/', views.TaskDetails.as_view(), name='todo-details'),

]
