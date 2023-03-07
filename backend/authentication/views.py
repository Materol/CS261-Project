from django.shortcuts import get_object_or_404
from dashboard.models import Project
from .serializers import ProjectSerializer
from rest_framework import generics, permissions


#This is the view of the main home page (all project view)
class ProjectList(generics.ListAPIView):
    #Must be authenticated
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    #CHANGE THIS: to query only the users' projects
    queryset = Project.objects.all()

#This is the view of a single project
class ProjectDetail(generics.RetrieveAPIView):
    #Must be authenticated
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer

    #Gets the project based on the slug (a bit added on the URL to identify individual projects)
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Project, slug=item)



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
    
