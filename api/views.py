from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from api.models import Todo
from api.serializers import TodoSerializer


class ApiRoot(APIView):
    def get(self, request):
        urls_list = {
            'task-list': 'tasks/',
        }
        return Response(urls_list, status=status.HTTP_200_OK)


class TaskList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, *kwargs)


class TaskDetails(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Shorter Form
# class TaskList(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#
#
# class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
