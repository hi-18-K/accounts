from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('register/', views.register , name = 'register'),
]
