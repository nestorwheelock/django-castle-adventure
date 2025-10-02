# T-002: Database Models Implementation

**Related Story:** S-002 (Story Navigation System)
**Priority:** P0 Critical
**Estimate:** 4 hours
**Sprint:** Sprint 1
**Status:** Pending

---

## AI Coding Brief

**Role:** Backend Django Developer
**Objective:** Implement all database models (Scene, Choice, Item, GameState, Ending) with relationships and migrations

**User Request:** "Create Django models for the story graph: scenes, choices, items, game state, and endings"

---

## Constraints

### Allowed File Paths
- `castle_adventure/models.py`
- `castle_adventure/migrations/`
- `castle_adventure/tests/test_models.py`

### Forbidden Paths
- No view logic yet (that's T-003)
- No content creation yet (that's T-010)

---

## Deliverables

### 1. Scene Model
```python
class Scene(models.Model):
    scene_id = models.CharField(max_length=10, unique=True)  # "01", "E1", "D1"
    title = models.CharField(max_length=200)
    description = models.TextField()
    ascii_art = models.TextField(blank=True)
    is_ending = models.BooleanField(default=False)
    is_death = models.BooleanField(default=False)
    scene_type = models.CharField(max_length=20, choices=SCENE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['scene_id']
```

### 2. Choice Model
```python
class Choice(models.Model):
    from_scene = models.ForeignKey(Scene, related_name='choices_from', on_delete=models.CASCADE)
    to_scene = models.ForeignKey(Scene, related_name='choices_to', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_letter = models.CharField(max_length=1)  # A, B, C, D
    requires_item = models.ForeignKey('Item', null=True, blank=True, on_delete=models.SET_NULL)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = [['from_scene', 'choice_letter']]
```

### 3. Item Model
```python
class Item(models.Model):
    item_id = models.CharField(max_length=20, unique=True)  # "ITEM_001"
    name = models.CharField(max_length=100)
    description = models.TextField()
    found_in_scene = models.ForeignKey(Scene, related_name='items_here', on_delete=models.CASCADE)
    is_critical = models.BooleanField(default=False)
    is_consumable = models.BooleanField(default=False)
    is_trap = models.BooleanField(default=False)
    icon = models.CharField(max_length=10, default='📦')  # Emoji icon
```

### 4. GameState Model
```python
class GameState(models.Model):
    # User identification
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)

    # Game progress
    current_scene = models.ForeignKey(Scene, related_name='active_games', on_delete=models.CASCADE)
    inventory = models.JSONField(default=list)  # ["ITEM_001", "ITEM_003"]
    visited_scenes = models.JSONField(default=list)  # ["01", "02", "03"]
    flags = models.JSONField(default=dict)  # {"dragon_befriended": True}

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
        return item_id in self.inventory

    def add_item(self, item_id):
        if item_id not in self.inventory:
            self.inventory.append(item_id)
            self.items_collected += 1
            self.save()
```

### 5. Ending Model
```python
class Ending(models.Model):
    ending_id = models.CharField(max_length=10, unique=True)  # "E1", "E2"
    title = models.CharField(max_length=200)
    description = models.TextField()
    ending_type = models.CharField(max_length=20, choices=ENDING_TYPES)
    icon = models.CharField(max_length=10)  # "⭐", "🗡️", etc.
    achievement_text = models.CharField(max_length=200)
    is_secret = models.BooleanField(default=False)
    requirements = models.JSONField(default=dict)
```

### 6. EndingUnlock Model
```python
class EndingUnlock(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    ending = models.ForeignKey(Ending, on_delete=models.CASCADE)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'ending'], ['session_key', 'ending']]
```

---

## Definition of Done

- [ ] All 6 models implemented in models.py
- [ ] Migrations created (`python manage.py makemigrations`)
- [ ] Migrations applied (`python manage.py migrate`)
- [ ] All model methods implemented (has_item, add_item, etc.)
- [ ] Admin registration for all models
- [ ] At least 23 tests written and passing (>95% coverage)
- [ ] Test database schema is correct
- [ ] Can create instances of all models
- [ ] Foreign key relationships work correctly
- [ ] JSON fields serialize/deserialize properly
- [ ] Code committed with "feat(models): implement database schema for story graph"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 23 tests:**
1-5. Scene model (create, unique scene_id, ordering, types, flags)
6-10. Choice model (create, foreign keys, unique together, ordering, item requirements)
11-14. Item model (create, found_in relationship, flags)
15-20. GameState model (create, inventory methods, flags, stats, user vs session)
21-22. Ending model (create, requirements)
23. EndingUnlock model (create, unique together)

---

## Dependencies

- **Blocks:** T-003 (views need models), T-004 (inventory needs models)
- **Depends on:** T-001 (app structure must exist)

---

**Created:** 2025-10-02
**Status:** Ready for Development
