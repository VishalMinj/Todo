from django.shortcuts import render
from rest_framework import viewsets
from .models import Tasks
from .serializers import TaskListSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TaskListSerializer
    
