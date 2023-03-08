#Building a simple template view for the dashboard

from django.urls import path
from django.views.generic import TemplateView
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('projects/<str:pk>/',
         views.ProjectDetail.as_view(),
         name='detail_project'),
    path('projects/', views.ProjectList.as_view(), name='list_project'),
    path('users/<str:pk>/', views.UserDetail.as_view(), name='detail_users'),
    path('users/', views.UserList.as_view(), name='list_users')
]
