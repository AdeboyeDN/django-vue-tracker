from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskListSerializers
from .models import task


class ApiListView(generics.ListCreateAPIView):
     queryset = task.objects.all()
     serializer_class = TaskListSerializers
