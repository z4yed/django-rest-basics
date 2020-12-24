from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='overview'),
    path('task-list/', views.todo_list, name='todo-list'),
]
