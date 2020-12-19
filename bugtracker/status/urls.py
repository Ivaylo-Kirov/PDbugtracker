from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="status-home"),
    path('contactadmin/', views.ContactFormView.as_view(), name="contact-admin")
]