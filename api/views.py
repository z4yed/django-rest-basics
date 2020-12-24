from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from api.models import Todo
from api.serializers import TodoSerializer
from django.shortcuts import get_object_or_404


class ApiOverview(APIView):
    def get(self, request):
        urls_list = {
            'list': '/task-list/',
            'details_view': '/task-detail/<task_id>/',
            'create': '/task-create',
            'update': '/task-update/<task_id>',
            'delete': '/task-delete/<task_id>/',
        }
        return Response(urls_list, status=status.HTTP_200_OK)


class TaskList(APIView):
    def get(self, request):
        tasks = Todo.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class TaskDetails(APIView):
    def get(self, request, task_id):
        todo = get_object_or_404(Todo, pk=task_id)
        serializer = TodoSerializer(todo, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, task_id):
        todo = get_object_or_404(Todo, pk=task_id)
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        todo = get_object_or_404(Todo, pk=task_id)
        todo.delete()
        return Response(status=status.HTTP_410_GONE)

# @api_view(['GET'])
# def api_overview(request):
#     urls_list = {
#         'list': '/task-list/',
#         'details_view': '/task-detail/<task_id>/',
#         'create': '/task-create',
#         'update': '/task-update/<task_id>',
#         'delete': '/task-delete/<task_id>/',
#     }
#     return Response(urls_list)
#

# @api_view(['GET'])
# def todo_list(request):
#     todos = Todo.objects.all()
#     serializers = TodoSerializer(todos, many=True)
#     return Response(serializers.data)
#
#
# @api_view(['GET'])
# def todo_details(request, task_id):
#     todo = Todo.objects.get(pk=task_id)
#     serializers = TodoSerializer(todo, many=False)
#     return Response(serializers.data)


# @api_view(['POST'])
# def create_todo(request):
#     serializers = TodoSerializer(data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#     return Response(serializers.data)
#
#
# @api_view(['POST'])
# def update_todo(request, task_id):
#     todo = Todo.objects.get(pk=task_id)
#     serializers = TodoSerializer(instance=todo, data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#     return Response(serializers.data)
#
#
# @api_view(['DELETE'])
# def delete_todo(request, task_id):
#     todo = Todo.objects.get(pk=task_id)
#     todo.delete()
#     return Response("Item Deleted Successfully. ")
