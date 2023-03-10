from django.db import models

#The main model for a project
class Project(models.Model):

    #Model fields
    name = models.TextField(default='')
    description = models.TextField(default='')
    CSFs = models.JSONField(default=dict)
    currentMetric = models.JSONField(default=dict)
    metricHistory = models.JSONField(default=dict)
    feedback = models.JSONField(default=dict)
    members = models.JSONField(default=dict)

    #Django object manager
    objects = models.Manager()

    def __str__(self):
        return self.name
  
