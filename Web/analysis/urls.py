from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("finedust/", views.finedust),
    path("social_economy/", views.social_economy),
    path("weather/", views.weather),
    path("aerosol/", views.aerosol),
]