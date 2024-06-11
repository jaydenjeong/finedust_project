from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("team/", views.teamintro),
    path("project/", views.projintro)
]