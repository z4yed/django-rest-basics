from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from api.models import Todo
from api.serializers import TodoSerializer

@api_view(['GET'])
def api_overview(request):
    urls_list = {
        'list': '/task-list/',
        'details_view': '/task/<str:pk>/',
        'create': '/task/create/',
        'update': '/task/update/<str:pk>',
        'delete': '/task/delete/<str:pk>/',
    }
    return Response(urls_list)


@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializers = TodoSerializer(todos, many=True)
    return Response(serializers.data)