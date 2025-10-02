from django.contrib import admin
from .models import Scene, Choice, Item, GameState, Ending, EndingUnlock


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    list_display = ['scene_id', 'title', 'scene_type', 'is_ending', 'is_death']
    list_filter = ['scene_type', 'is_ending', 'is_death']
    search_fields = ['scene_id', 'title', 'description']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['from_scene', 'choice_letter', 'choice_text', 'to_scene', 'requires_item']
    list_filter = ['from_scene']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'name', 'found_in_scene', 'is_critical', 'is_consumable', 'is_trap']
    list_filter = ['is_critical', 'is_consumable', 'is_trap']


@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    list_display = ['user', 'session_key', 'current_scene', 'choices_made', 'items_collected', 'is_complete']
    list_filter = ['is_complete']


@admin.register(Ending)
class EndingAdmin(admin.ModelAdmin):
    list_display = ['ending_id', 'title', 'ending_type', 'is_secret']
    list_filter = ['ending_type', 'is_secret']


@admin.register(EndingUnlock)
class EndingUnlockAdmin(admin.ModelAdmin):
    list_display = ['user', 'session_key', 'ending', 'unlocked_at']
    list_filter = ['ending']
