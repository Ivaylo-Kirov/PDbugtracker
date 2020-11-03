from django.shortcuts import render, get_object_or_404
from .models import Project, Bug
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django import forms

# Create your views here.
def home(request):
        
    #latest_bugs = Project.bug_set.all().order_by('date_added')[:3]
    projects = Project.objects.filter(editors=request.user)
    #bugs = projects.first().bug_set.all() #how do I filter this on a per project basis, right now it just returns bugs for the first project

    #.bug_set.all().order_by('date_added')
    context = {
        'projects': projects,
        #'latest_bugs': bugs,
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


class BugCreateSupportForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['name', 'desc', 'image', 'bug_type', 'project']
        widgets = {
            'desc': forms.Textarea
        }

class BugCreateView(LoginRequiredMixin, CreateView):
    form_class = BugCreateSupportForm # form_class allows you to use forms.ModelForm and utilize functionality like widgets
    model = Bug

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BugUpdateSupportForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['name', 'desc', 'image', 'bug_type']
        widgets = {
            'desc': forms.Textarea
        }

class BugUpdateView(LoginRequiredMixin, UpdateView):
    form_class = BugUpdateSupportForm 
    model = Bug

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)