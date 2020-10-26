from django.shortcuts import render
from .models import Project

projects = [
    {'name': 'First Project'},
    {'name': 'Second Project'}
]

# Create your views here.
def home(request):
    context = {
        'projects': Project.objects.all(),
        'title': 'Projects'
    }
    return render(request, 'projects/home.html', context)