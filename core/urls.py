from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workshops/', views.workshops, name='workshops'),
    path('labs/', views.labs, name='labs'),
    path('store/', views.store, name='store'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
