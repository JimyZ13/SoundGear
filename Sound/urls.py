from django.urls import path

from . import views

urlpatterns = [
    path('HelloWorld/', views.index),
    path('Test/', views.text),
]