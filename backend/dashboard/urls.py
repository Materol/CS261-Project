#Building a simple template view for the dashboard

from django.urls import path
from django.views.generic import TemplateView
from dashboard import views

app_name = 'dashboard'

#Paths for projects
urlpatterns = [
    path('projects/detail/<str:pk>/',
         views.ProjectDetail.as_view(),
         name='detail_project'),
    path('projects/delete/<str:pk>/',
         views.DeleteProject.as_view(),
         name='delete_project'),
    path('projects/create/',
         views.CreateProject.as_view(),
         name='create_project'),
    path('projects/', views.ProjectList.as_view(), name='list_project'),
    # path('users/<str:pk>/', views.UserDetail.as_view(), name='detail_users'),
    # path('users/', views.UserList.as_view(), name='list_users')
]
