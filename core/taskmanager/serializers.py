from rest_framework import serializers
from taskmanager.models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "deadline",
            "created_at",
            "status",
            "priority",
            "category",
        ]
