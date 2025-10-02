"""
URL configuration for running tests.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('castle_adventure.urls')),
]
