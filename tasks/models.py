from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    user = models.ForeignKey(User, related_name='task')
    collaborator1 = models.ForeignKey(User, related_name='task', null=True)
    collaborator2 = models.ForeignKey(User, related_name='task', null=True)
    collaborator3 = models.ForeignKey(User, related_name='task', null=True)
    complete = models.BooleanField(default=False)
