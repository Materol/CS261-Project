from django.shortcuts import get_object_or_404
from dashboard.models import Project
from .serializers import ProjectSerializer
from rest_framework import generics, permissions


#This is the view of the main home page (all project view)
class ProjectList(generics.ListAPIView):
    #Must be authenticated
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

#This is the view of a single project for the admin
class ProjectDetail(generics.RetrieveAPIView):
    #Must be authenticated
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer


#CRUD operations for admin, will remain the same but be applied for all users
class CreateProject(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AdminProjectDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EditProject(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class DeleteProject(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    
