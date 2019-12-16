from django.contrib import admin
from django.urls import path
from parsing.views import main

urlpatterns = [
    path('', main, name='main'),
]