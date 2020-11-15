from django.shortcuts import render, get_object_or_404
from .models import Project, Bug, Comment
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.http import HttpResponse, Http404

# Create your views here.
@login_required
def home(request):
    projects = Project.objects.filter(editors=request.user)
    #bugs = projects.first().bug_set.all() #how do I filter this on a per project basis, right now it just returns bugs for the first project

    context = {
        'projects': projects,
        'title': 'Projects'
    }
    return render(request, 'projects/home.html', context)

@require_GET
def search_results(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        bugs = Bug.objects.filter(desc__icontains=q)
        return render(request, 'projects/search_results.html', {'bugs': bugs, 'query': q})
    else:
        raise Http404("Invalid Search")

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


############
## CREATE ##
############
class BugCreateSupportForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['name', 'desc', 'image', 'image2', 'bug_type', 'project']
        widgets = {
            'desc': forms.Textarea
        }

class BugCreateView(LoginRequiredMixin, CreateView):
    form_class = BugCreateSupportForm # form_class allows you to use forms.ModelForm and utilize functionality like widgets
    model = Bug

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['desc', 'image']

    def form_valid(self, form):
        bug = get_object_or_404(Bug, id=self.kwargs.get('id'))
        form.instance.bug = bug
        form.instance.author = self.request.user
        return super().form_valid(form)
############
############





############
## UPDATE ##
############
class BugUpdateSupportForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['name', 'desc', 'image', 'image2', 'bug_type']
        widgets = {
            'desc': forms.Textarea
        }

class BugUpdateView(LoginRequiredMixin, UpdateView):
    form_class = BugUpdateSupportForm 
    model = Bug

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
############
############