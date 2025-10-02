"""
URL configuration for castle_adventure app.
"""
from django.urls import path
from . import views

app_name = 'castle_adventure'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('start/', views.start_game, name='start'),
    path('new/', views.new_game, name='new_game'),
    path('scene/<str:scene_id>/', views.display_scene, name='scene'),
    path('choice/<int:choice_id>/', views.make_choice, name='choice'),
    path('pickup/<str:item_id>/', views.pickup_item, name='pickup_item'),
    path('inventory/', views.view_inventory, name='inventory'),
    path('save/', views.save_game, name='save'),
    path('load/', views.load_game, name='load'),
    path('ending/<str:scene_id>/', views.display_ending, name='display_ending'),
    path('endings/', views.endings_collection, name='endings_collection'),
]
