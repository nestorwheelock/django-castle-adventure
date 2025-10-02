"""
Database models for Castle Adventure game.
Implements story graph, game state, and progression tracking.
"""
from django.db import models
from django.contrib.auth.models import User


class Scene(models.Model):
    """A scene/location in the story graph."""

    SCENE_TYPES = [
        ('story', 'Story Scene'),
        ('death', 'Death Scene'),
        ('ending', 'Ending Scene'),
        ('hub', 'Hub Scene'),
    ]

    scene_id = models.CharField(max_length=10, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ascii_art = models.TextField(blank=True)
    is_ending = models.BooleanField(default=False)
    is_death = models.BooleanField(default=False)
    scene_type = models.CharField(max_length=20, choices=SCENE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['scene_id']

    def __str__(self):
        return f"{self.scene_id}: {self.title}"


class Item(models.Model):
    """An item that can be found and used in the game."""

    item_id = models.CharField(max_length=20, unique=True, db_index=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    found_in_scene = models.ForeignKey(
        Scene,
        related_name='items_here',
        on_delete=models.CASCADE
    )
    is_critical = models.BooleanField(default=False)
    is_consumable = models.BooleanField(default=False)
    is_trap = models.BooleanField(default=False)
    icon = models.CharField(max_length=10, default='📦')

    def __str__(self):
        return f"{self.item_id}: {self.name}"


class Choice(models.Model):
    """A choice/action connecting two scenes."""

    from_scene = models.ForeignKey(
        Scene,
        related_name='choices_from',
        on_delete=models.CASCADE
    )
    to_scene = models.ForeignKey(
        Scene,
        related_name='choices_to',
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    choice_letter = models.CharField(max_length=1)
    requires_item = models.ForeignKey(
        Item,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = [['from_scene', 'choice_letter']]

    def __str__(self):
        return f"[{self.choice_letter}] {self.choice_text}"


class GameState(models.Model):
    """Tracks a player's current game progress."""

    # User identification (user OR session_key)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    session_key = models.CharField(max_length=40, null=True, blank=True)

    # Game progress
    current_scene = models.ForeignKey(
        Scene,
        related_name='active_games',
        on_delete=models.CASCADE
    )
    inventory = models.JSONField(default=list)
    visited_scenes = models.JSONField(default=list)
    flags = models.JSONField(default=dict)

    # Metadata
    game_started = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    ending_reached = models.CharField(max_length=10, null=True, blank=True)

    # Stats
    choices_made = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    items_collected = models.IntegerField(default=0)

    def has_item(self, item_id):
        """Check if item is in inventory."""
        return item_id in self.inventory

    def add_item(self, item_id):
        """Add item to inventory if not already present."""
        if item_id not in self.inventory:
            self.inventory.append(item_id)
            self.items_collected += 1
            self.save()

    def __str__(self):
        user_display = self.user.username if self.user else f"Session {self.session_key[:8]}"
        return f"{user_display} - {self.current_scene.title}"


class Ending(models.Model):
    """A possible ending to the game."""

    ENDING_TYPES = [
        ('victory', 'Victory'),
        ('defeat', 'Defeat'),
        ('betrayal', 'Betrayal'),
        ('comedy', 'Comedy'),
        ('secret', 'Secret'),
    ]

    ending_id = models.CharField(max_length=10, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ending_type = models.CharField(max_length=20, choices=ENDING_TYPES)
    icon = models.CharField(max_length=10)
    achievement_text = models.CharField(max_length=200)
    is_secret = models.BooleanField(default=False)
    requirements = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.ending_id}: {self.title}"


class EndingUnlock(models.Model):
    """Tracks which endings a user has unlocked."""

    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    session_key = models.CharField(max_length=40, null=True, blank=True)
    ending = models.ForeignKey(Ending, on_delete=models.CASCADE)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'ending'], ['session_key', 'ending']]

    def __str__(self):
        user_display = self.user.username if self.user else f"Session {self.session_key[:8]}"
        return f"{user_display} unlocked {self.ending.title}"
