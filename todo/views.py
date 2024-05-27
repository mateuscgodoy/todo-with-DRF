from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Todo
from .permissions import IsOwnerOrReadOnly
from .serializers import TodoSerializer, UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    A view set to automatically `list`, `create`, `retrieve`
    `update`, and `destroy` todos
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    A view set to automatically `list`, `retrieve` users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
