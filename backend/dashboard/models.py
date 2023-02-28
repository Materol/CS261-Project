
from django.db import models
from django.utils import timezone
from django.conf import settings



#The main model for out project - switch / adapt with pav database if necessary
class Project(models.Model):

    #Model fields
    title = models.CharField(max_length=250)
    Description = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creator_projects')

    #Django object manager
    objects = models.Manager()

    #Ordering when showed
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title























