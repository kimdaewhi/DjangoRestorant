from django.contrib import admin
from django.urls import path
from foods import views

urlpatterns = [
    path('index/', views.index),
]
