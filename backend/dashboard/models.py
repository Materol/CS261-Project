from django.db import models
from django.utils import timezone
from django.conf import settings



#The main model for a project
class Project(models.Model):

    #Model fields
    name = models.TextField()
    Description = models.TextField()
    currenMetric = models.JSONField()
    metricHistory = models.JSONField()
    members = models.JSONField()

    #Django object manager
    objects = models.Manager()

    def __str__(self):
        return self.name
    
    
class ProjectHistory(models.Model):

    #Model fields
    name = models.TextField()
    Description = models.TextField()
    currenMetric = models.JSONField()
    metricHistory = models.JSONField()
    members = models.JSONField()

    #Django object manager
    objects = models.Manager()

    def __str__(self):
        return self.name























