from django.urls import path
from django.views.generic import TemplateView
from blog import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
]