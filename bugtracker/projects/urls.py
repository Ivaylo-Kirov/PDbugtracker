from django.urls import path
from . import views
from .views import BugListView, BugCreateView, BugDetailView, BugUpdateView, BugProjectListView, BugDeleteView, CommentCreateView, CommentDeleteView

urlpatterns = [
    path('', views.home, name="projects-home"),
    path('bugs/', BugListView.as_view(), name="bugs-list"),
    path('bugs/create/', BugCreateView.as_view(), name="bugs-create"),
    path('bugs/create/comment/<int:id>', CommentCreateView.as_view(), name="bugs-create-comment"),
    path('bugs/detail/<int:pk>', BugDetailView.as_view(), name="bugs-detail"),
    path('bugs/update/<int:pk>', BugUpdateView.as_view(), name="bugs-update"),
    path('bugs/delete/<int:pk>', BugDeleteView.as_view(), name="bugs-delete"),
    path('bugs/delete/comment/<int:pk>', CommentDeleteView.as_view(), name="comment-delete"),
    path('bugs/project/<int:id>', BugProjectListView.as_view(), name="bugs-project"),
    path('search-results/', views.search_results, name="search-results")
]