# T-007: Story Content Database Population

**Related Story:** S-006 (Story Content Implementation)
**Priority:** P0 Critical
**Estimate:** 6 hours
**Sprint:** Sprint 2 & 3
**Status:** Pending

---

## AI Coding Brief

**Role:** Content Writer + Backend Developer
**Objective:** Write all 28 scene descriptions, create database fixtures, and populate story content

**User Request:** "Write all story scenes, items, choices, and endings then load them into the database"

---

## Constraints

### Allowed File Paths
- `castle_adventure/fixtures/` (new directory)
- `castle_adventure/fixtures/scenes.json`
- `castle_adventure/fixtures/choices.json`
- `castle_adventure/fixtures/items.json`
- `castle_adventure/fixtures/endings.json`
- `castle_adventure/management/commands/load_story_content.py`
- `castle_adventure/tests/test_content.py`

### Forbidden Paths
- No ASCII art yet (that's T-008)

---

## Deliverables

### 1. Scene Content (28 scenes)

**Use story-graph.md as reference. Create JSON fixtures:**

```json
[
  {
    "model": "castle_adventure.scene",
    "pk": 1,
    "fields": {
      "scene_id": "01",
      "title": "Outside Castle Walls",
      "description": "Dark, stormy night. Castle Shadowmere looms ominously before you...",
      "scene_type": "story",
      "is_ending": false,
      "is_death": false,
      "ascii_art": ""
    }
  },
  ...
]
```

**All 28 scenes from story-graph.md:**
- 21 story scenes (01-23)
- 6 death scenes (D1-D8)
- 5 ending scenes (E1-E5)

### 2. Choice Content (~85 choices)

```json
[
  {
    "model": "castle_adventure.choice",
    "pk": 1,
    "fields": {
      "from_scene": 1,  # Scene 01
      "to_scene": 2,    # Scene 02
      "choice_text": "Climb the garden wall (stealthy)",
      "choice_letter": "A",
      "requires_item": null,
      "order": 1
    }
  },
  ...
]
```

### 3. Item Content (8 items)

```json
[
  {
    "model": "castle_adventure.item",
    "pk": 1,
    "fields": {
      "item_id": "ITEM_001",
      "name": "Magic Spectacles",
      "description": "Dusty spectacles that reveal what eyes cannot see...",
      "found_in_scene": 13,  # Troll's Lair
      "is_critical": true,
      "is_consumable": false,
      "is_trap": false,
      "icon": "🔮"
    }
  },
  ...
]
```

### 4. Ending Content (5 endings)

```json
[
  {
    "model": "castle_adventure.ending",
    "pk": 1,
    "fields": {
      "ending_id": "E1",
      "title": "Heroic Rescue",
      "description": "Princess Elara carefully evaluates you...",
      "ending_type": "victory",
      "icon": "⭐",
      "achievement_text": "The classic ending. Well done!",
      "is_secret": false,
      "requirements": {}
    }
  },
  ...
]
```

### 5. Management Command to Load Content

```python
# management/commands/load_story_content.py
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load all story content from fixtures'

    def handle(self, *args, **options):
        self.stdout.write('Loading story content...')

        call_command('loaddata', 'scenes')
        call_command('loaddata', 'choices')
        call_command('loaddata', 'items')
        call_command('loaddata', 'endings')

        self.stdout.write(self.style.SUCCESS('Story content loaded successfully!'))
```

---

## Writing Standards

**Scene Descriptions:**
- 3-5 sentences
- Atmospheric and engaging
- Dark humor tone
- Clear setup for choices

**Death Scenes:**
- Humorous description of failure
- Self-aware narrator
- Encourages retry

**Endings:**
- 180-250 words
- Satisfying conclusion
- References player's journey
- Distinct from other endings

---

## Definition of Done

- [ ] All 28 scenes written with descriptions
- [ ] All ~85 choices defined with connections
- [ ] All 8 items written with descriptions
- [ ] All 5 endings written (full text from endings.md)
- [ ] JSON fixtures created for all content
- [ ] Management command to load content
- [ ] Story graph integrity validated (no orphans, all paths work)
- [ ] At least 10 content validation tests passing
- [ ] Can load fixtures: `python manage.py load_story_content`
- [ ] Critical path playthrough works (Scene 01 → E1)
- [ ] Code committed with "feat(content): add all story scenes, items, and endings"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 10 tests:**
1. All 28 scenes loaded
2. All choices loaded and valid
3. All items loaded
4. All endings loaded
5. No orphaned scenes
6. Critical path is playable
7. All item requirements satisfied
8. At least 3 endings reachable
9. Death scenes properly flagged
10. Ending scenes properly flagged

---

## Dependencies

- **Blocks:** T-009 (templates need content to display)
- **Depends on:** T-002 (models), T-003 (views)

---

**Created:** 2025-10-02
**Status:** Ready for Development
