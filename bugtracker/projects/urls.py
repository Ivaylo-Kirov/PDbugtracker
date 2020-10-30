from django.urls import path
from . import views
from .views import BugListView, BugCreateView, BugDetailView, BugUpdateView

urlpatterns = [
    path('', views.home, name="projects-home"),
    path('bugs/', BugListView.as_view(), name="bugs-list"),
    path('bugs/create/', BugCreateView.as_view(), name="bugs-create"),
    path('bugs/detail/<int:pk>', BugDetailView.as_view(), name="bugs-detail"),
    path('bugs/update/<int:pk>', BugUpdateView.as_view(), name="bugs-update"),
]