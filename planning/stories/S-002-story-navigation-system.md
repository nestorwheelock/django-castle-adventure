# S-002: Story Navigation System

**Story Type**: User Story
**Priority**: High
**Estimate**: 2 days
**Sprint**: Sprint 1
**Status**: ✅ Planned (awaiting approval)

---

## User Story

**As a** player
**I want to** navigate through the castle story by making choices
**So that** I can experience the adventure and explore different paths

---

## Acceptance Criteria

- [ ] When I start a new game, I see the first scene (Outside Castle Walls)
- [ ] When I read a scene, I see the description and available choices
- [ ] When I make a choice, I navigate to the next scene
- [ ] When I reach a dead-end (death scene), I can restart
- [ ] When I reach an ending, I see the ending text and can start a new game
- [ ] When I try to make an invalid choice, I get a clear error message
- [ ] When a choice requires an item I don't have, it is disabled or marked as locked

---

## Definition of Done

- [ ] Scene model implemented with title, description, ascii_art, is_ending fields
- [ ] Choice model implemented linking scenes with choice_text and requirements
- [ ] Game navigation view handles scene transitions (23 tests minimum)
- [ ] All 28 scenes from story-graph.md implemented in database
- [ ] All scene connections validated (no orphaned scenes)
- [ ] Critical path playable (START → Scene 01 → ... → E1)
- [ ] Tests written for graph integrity (>95% coverage)
- [ ] Code committed with reference to this story

---

## Story Graph Requirements

**Must implement:**
- 21 story scenes
- 6 death scenes
- 5 ending scenes
- 3 convergence hubs (Scenes 07, 09, 19)
- ~85 choices total

**Graph Validation Tests:**
- No orphaned scenes (unreachable from START)
- No dead-ends (except deaths and endings)
- All choices lead to valid scenes
- Critical path is playable
- At least 3 endings reachable

---

## Database Models

**Scene Model:**
```python
class Scene(models.Model):
    scene_id = models.CharField(max_length=10, unique=True)  # "01", "E1", "D1"
    title = models.CharField(max_length=200)
    description = models.TextField()
    ascii_art = models.TextField(blank=True)
    is_ending = models.BooleanField(default=False)
    is_death = models.BooleanField(default=False)
    scene_type = models.CharField(max_length=20)  # story/death/ending/hub
```

**Choice Model:**
```python
class Choice(models.Model):
    from_scene = models.ForeignKey(Scene, related_name='choices_from')
    to_scene = models.ForeignKey(Scene, related_name='choices_to')
    choice_text = models.CharField(max_length=200)
    choice_letter = models.CharField(max_length=1)  # A, B, C, D
    requires_item = models.ForeignKey(Item, null=True, blank=True)
    order = models.IntegerField(default=0)
```

---

## API Endpoints

**Required Views:**
- `/start/` - Start new game (initialize state, go to Scene 01)
- `/scene/<scene_id>/` - Display current scene with choices
- `/choice/<choice_id>/` - Make a choice, navigate to next scene
- `/restart/` - Restart game after death

---

## Testing Requirements

**Unit Tests:**
- Scene model creation
- Choice model with requirements
- Scene navigation logic
- Invalid choice handling

**Integration Tests:**
- Complete critical path playthrough (START → E1)
- Alternate path playthrough (START → E2, E3)
- Dead-end handling (death scenes)
- Locked choice behavior (item requirements)

---

## Related Stories

- Depends on: S-001 (Django module structure)
- Blocks: S-006 (Story content depends on navigation working)
- Related: S-003 (Inventory affects choice availability)

---

**Document Status:** Ready for Development
**Created:** 2025-10-02
