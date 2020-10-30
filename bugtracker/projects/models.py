from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    PROJ_TYPES = (
        ('D', 'Dev'),
        ('P', 'Print'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=60)
    proj_type = models.CharField(max_length=1, choices=PROJ_TYPES)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    editors = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Bug(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    desc = models.CharField(max_length=200)
    BUG_TYPES = (
        ('V', 'Visual'),
        ('L', 'Logical'),
        ('O', 'Other'),
    )
    bug_type = models.CharField(max_length=1, choices=BUG_TYPES)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'Bug ID: {self.id}'
    
    def get_absolute_url(self):
        return reverse('bugs-detail', kwargs={'pk': self.pk})