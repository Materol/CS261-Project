from django.db import models
from django.utils import timezone
from django.conf import settings



#The main model for a project
class Project(models.Model):

    #Model fields
    name = models.TextField(default='')
    Description = models.TextField(default='')
    currentMetric = models.JSONField(default='')
    metricHistory = models.JSONField(default='')
    members = models.JSONField(default='')

    #Django object manager
    objects = models.Manager()

    def __str__(self):
        return self.name
    
























