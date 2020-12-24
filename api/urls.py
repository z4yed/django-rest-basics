from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name='api-root'),
    path('tasks/', views.TaskList.as_view(), name='task_list_create'),
    path('tasks/<pk>', views.TaskDetails.as_view(), name='task_details_update_delete'),
]
