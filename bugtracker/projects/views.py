from django.shortcuts import render, get_object_or_404
from .models import Project, Bug
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
    paginate_by = 5

class BugProjectListView(LoginRequiredMixin, ListView):
    model = Bug
    paginate_by = 5

    template_name="projects/project_bugs.html"

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get('id'))
        return Bug.objects.filter(project=project)

class BugDetailView(LoginRequiredMixin, DetailView):
    model = Bug

class BugDeleteView(LoginRequiredMixin, DeleteView):
    model = Bug
    success_url = reverse_lazy('bugs-list')

class BugCreateView(LoginRequiredMixin, CreateView):
    model = Bug
    fields = ['name', 'desc', 'image', 'bug_type', 'project']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BugUpdateView(LoginRequiredMixin, UpdateView):
    model = Bug
    fields = ['name', 'desc', 'image', 'bug_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)