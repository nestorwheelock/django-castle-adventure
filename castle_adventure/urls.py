"""
URL configuration for castle_adventure app.
"""
from django.urls import path
from . import views

app_name = 'castle_adventure'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('start/', views.start_game, name='start'),
    path('scene/<str:scene_id>/', views.display_scene, name='scene'),
    path('choice/<int:choice_id>/', views.make_choice, name='choice'),
    path('pickup/<str:item_id>/', views.pickup_item, name='pickup_item'),
    path('inventory/', views.view_inventory, name='inventory'),
    path('save/', views.save_game, name='save'),
    path('load/', views.load_game, name='load'),
]
