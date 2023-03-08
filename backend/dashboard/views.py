from .models import Project
from .serializers import ProjectSerializerDashboard, CustomUserSerializer
from rest_framework import generics, permissions
from users.models import NewUser
from rest_framework.permissions import BasePermission, SAFE_METHODS
# Create your views here.


class PostUserWritePermission(BasePermission):
    messeage = 'Editing this project is restricted to the creator only'

    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True

        return obj.creator == request.user


class UserList(generics.ListAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer


class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializerDashboard

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(creator=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(creator=user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView,
                    PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerDashboard
