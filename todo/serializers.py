from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Todo
        fields = ["url", "id", "text", "completed", "owner"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedIdentityField(
        many=True, view_name="todo-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "todos"]
