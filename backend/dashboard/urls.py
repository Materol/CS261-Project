#Building a simple template view for the dashboard

from django.urls import path
from django.views.generic import TemplateView
from dashboard import views

app_name = 'dashboard'

#Paths for projects
urlpatterns = [
    path('api/projects/detail/<str:pk>/',
         views.ProjectDetail.as_view(),
         name='detail_project'),
    path('api/projects/delete/<str:pk>/',
         views.DeleteProject.as_view(),
         name='delete_project'),
    path('api/projects/create/',
         views.CreateProject.as_view(),
         name='create_project'),
    path('api/projects/<str:user_email>', views.ProjectList.as_view(), name='list_project'),
]
