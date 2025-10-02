# T-005: Save and Load Game State System

**Related Story:** S-004 (Save/Load System)
**Priority:** P0 Critical
**Estimate:** 2 hours
**Sprint:** Sprint 2
**Status:** Pending

---

## AI Coding Brief

**Role:** Backend Django Developer
**Objective:** Implement auto-save and manual save/load functionality for game state

**User Request:** "Create save and load game functionality with auto-save on every action and manual save option"

---

## Constraints

### Allowed File Paths
- `castle_adventure/views.py` (add to existing)
- `castle_adventure/tests/test_save_load.py`

### Forbidden Paths
- No UI implementation yet (that's T-009)

---

## Deliverables

### 1. Auto-Save on Every Action
Modify existing views to auto-save:
```python
def make_choice(request, choice_id):
    # ... existing code ...
    game_state.save()  # Auto-save after state update
    return redirect(...)
```

### 2. Manual Save View
```python
def save_game(request):
    """Manually save game state."""
    game_state = get_game_state(request)
    game_state.save()

    return JsonResponse({
        'success': True,
        'message': 'Game saved successfully',
        'last_saved': game_state.last_updated.isoformat(),
    })
```

### 3. Load Game View
```python
def load_game(request):
    """Load existing game state."""
    game_state = get_or_create_game_state(request)

    if not game_state:
        return JsonResponse({
            'success': False,
            'message': 'No saved game found'
        }, status=404)

    return redirect('castle_adventure:scene', scene_id=game_state.current_scene.scene_id)
```

### 4. New Game with Overwrite Confirmation
```python
def new_game(request):
    """Start new game, optionally overwriting existing save."""
    existing_save = get_or_create_game_state(request)

    if existing_save and not request.POST.get('confirm_overwrite'):
        return JsonResponse({
            'requires_confirmation': True,
            'existing_save': {
                'scene': existing_save.current_scene.title,
                'items': existing_save.items_collected,
                'last_played': existing_save.last_updated.isoformat(),
            }
        })

    # Delete old save if exists
    if existing_save:
        existing_save.delete()

    # Create new game
    return redirect('castle_adventure:start')
```

---

## Definition of Done

- [ ] Auto-save occurs on every game state change
- [ ] Manual save view works
- [ ] Load game restores state correctly
- [ ] New game with overwrite confirmation
- [ ] Save state persists across sessions
- [ ] Anonymous users use session-based saves
- [ ] Authenticated users use user-based saves
- [ ] At least 15 tests written and passing (>95% coverage)
- [ ] Code committed with "feat(save): implement save and load game state system"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 15 tests:**
1-3. Auto-save (saves on choice, saves on item pickup, updates last_updated)
4-5. Manual save (success, no active game)
6-8. Load game (loads existing, no save found, restores correct scene)
9-11. New game (creates fresh state, overwrite confirmation, deletes old save)
12-13. Session vs user saves (anonymous user, authenticated user)
14-15. Integration (save → logout → login → load → state preserved)

---

## Dependencies

- **Blocks:** None (feature complete on its own)
- **Depends on:** T-002 (GameState model), T-003 (views structure)

---

**Created:** 2025-10-02
**Status:** Ready for Development
