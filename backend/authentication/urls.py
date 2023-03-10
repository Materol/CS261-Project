from .views import ProjectList, ProjectDetail, CreateProject, EditProject, AdminProjectDetail, DeleteProject
from django.urls import path

app_name = 'authentication'

#These are the URLS for the admin pages
urlpatterns = [
    path('', ProjectList.as_view(), name='listproject'),
    #To view individual project - deprecated to projects/
    path('project/<str:pk>/', ProjectDetail.as_view(), name='detailproject'),
    #CRUD for admin
    path('admin/edit/<int:pk>/', EditProject.as_view(), name='editproject'),
    path('admin/delete/<int:pk>/',
         DeleteProject.as_view(),
         name='deleteproject'),
    path('admin/create/', CreateProject.as_view(), name='createproject'),
    path('admin/edit/projectdetail/<int:pk>/',
         AdminProjectDetail.as_view(),
         name='admindetailproject'),
]
