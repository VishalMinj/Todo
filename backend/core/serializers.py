from rest_framework import serializers
from .models import Tasks


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        fields='__all__'

