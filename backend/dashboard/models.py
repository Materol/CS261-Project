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
    Budget = models.IntegerField(default=1000)
    riskiness = models.IntegerField(default=10)
    StartingDate = models.DateField(default=timezone.now)
    Deadline = models.DateField(default=timezone.now)
    Member_size = models.IntegerField(default=3)
    Completed = models.BooleanField(default=False)

    #Django object manager
    objects = models.Manager()

    #Ordering when showed
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title























