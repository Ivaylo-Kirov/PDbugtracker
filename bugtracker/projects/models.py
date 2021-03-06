from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=50)
    PROJ_TYPES = (
        ('D', 'Dev'),
        ('P', 'Print'),
        ('O', 'Other'),
    )
    proj_type = models.CharField(max_length=1, choices=PROJ_TYPES)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    editors = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Bug(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=2000, help_text="2000 character limit.")
    BUG_TYPES = (
        ('V', 'Visual'),
        ('L', 'Logical'),
        ('O', 'Other'),
    )
    bug_type = models.CharField(max_length=1, choices=BUG_TYPES)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='bug_pics', default='default_bug.png') #image field has automatic validation to ensure the upload is a valid image - no need for further validation on file size since we are using Pillow to resize to a manageable size
    image2 = models.ImageField(upload_to='bug_pics', default='default_bug.png')

    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'Bug ID: {self.id}'
    
    def get_absolute_url(self):
        return reverse('bugs-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    desc = models.CharField(max_length=1000, help_text="1000 character limit.")
    date_added = models.DateTimeField(auto_now_add=True)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='bug_pics', default='default_bug.png')

    def get_absolute_url(self):
        return reverse('bugs-detail', kwargs={'pk': self.bug.pk})

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return f'Comment ID: {self.id}'