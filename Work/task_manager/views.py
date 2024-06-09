from rest_framework import generics, permissions
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from task_manager.permissions import IsOwnerOrReadOnly
from task_manager.models import Task
from task_manager.serializers import serializers
from rest_framework import generics

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskDetail(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

class TaskClose(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        # Здесь логика для проверки, что отчет не пустой
        serializer.save()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class MyModelList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MyModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)