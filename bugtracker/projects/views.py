from django.shortcuts import render
from .models import Project, Bug
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

projects = [
    {'name': 'First Project'},
    {'name': 'Second Project'}
]

# Create your views here.
def home(request):
        
    context = {
        'projects': Project.objects.filter(editors=request.user),
        'title': 'Projects'
    }
    return render(request, 'projects/home.html', context)

class BugListView(LoginRequiredMixin, ListView):
    model = Bug
    ordering = ['-date_added']

class BugDetailView(LoginRequiredMixin, DetailView):
    model = Bug

class BugCreateView(LoginRequiredMixin, CreateView):
    model = Bug
    fields = ['desc', 'bug_type', 'project']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BugUpdateView(LoginRequiredMixin, UpdateView):
    model = Bug
    fields = ['desc', 'bug_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)