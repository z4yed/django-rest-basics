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
        'details_view': '/task-detail/<task_id>/',
        'create': '/task-create',
        'update': '/task-update/<task_id>',
        'delete': '/task-delete/<task_id>/',
    }
    return Response(urls_list)


@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializers = TodoSerializer(todos, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def todo_details(request, task_id):
    todo = Todo.objects.get(pk=task_id)
    serializers = TodoSerializer(todo, many=False)
    return Response(serializers.data)


@api_view(['POST'])
def create_todo(request):
    serializers = TodoSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['POST'])
def update_todo(request, task_id):
    todo = Todo.objects.get(pk=task_id)
    serializers = TodoSerializer(instance=todo, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['DELETE'])
def delete_todo(request, task_id):
    todo = Todo.objects.get(pk=task_id)
    todo.delete()
    return Response("Item Deleted Successfully. ")
