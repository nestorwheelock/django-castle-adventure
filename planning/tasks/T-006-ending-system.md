# T-006: Multiple Endings Determination System

**Related Story:** S-005 (Multiple Endings System)
**Priority:** P1 Important
**Estimate:** 3 hours
**Sprint:** Sprint 2
**Status:** Pending

---

## AI Coding Brief

**Role:** Backend Django Developer
**Objective:** Implement ending determination logic, ending unlock tracking, and ending display

**User Request:** "Create logic to determine which ending the player reaches based on their choices, items, and flags"

---

## Constraints

### Allowed File Paths
- `castle_adventure/views.py` (add to existing)
- `castle_adventure/ending_logic.py` (new file for determination algorithm)
- `castle_adventure/tests/test_endings.py`

### Forbidden Paths
- No ending content yet (that's T-007)

---

## Deliverables

### 1. Ending Determination Logic
```python
# ending_logic.py
def determine_ending(game_state):
    """
    Determine which ending player reaches based on game state.
    Returns ending_id (E1-E5).
    """
    items = game_state.inventory
    flags = game_state.flags

    # E5: Secret Ending (most specific first)
    if (len(items) == 8 and
        all_npcs_befriended(flags) and
        flags.get('sat_on_throne')):
        return 'E5'

    # E4: Castle Collapse
    if flags.get('chaos_level', 0) > 10:
        return 'E4'

    # E3: Mutual Escape
    if ('ITEM_004' in items and
        flags.get('dragon_befriended') and
        flags.get('troll_befriended') and
        flags.get('wizard_helped')):
        return 'E3'

    # E2: Tragic Betrayal
    if flags.get('npc_relations', 0) < 0 or flags.get('killed_npcs'):
        return 'E2'

    # E1: Heroic Rescue (default)
    return 'E1'

def all_npcs_befriended(flags):
    """Check if all NPCs were befriended."""
    return (flags.get('dragon_befriended') and
            flags.get('troll_befriended') and
            flags.get('wizard_helped'))
```

### 2. Ending View
```python
def display_ending(request, scene_id):
    """Display ending with achievement unlock."""
    game_state = get_game_state(request)
    scene = get_object_or_404(Scene, scene_id=scene_id, is_ending=True)

    # Determine which ending
    ending_id = determine_ending(game_state)
    ending = Ending.objects.get(ending_id=ending_id)

    # Mark game as complete
    game_state.is_complete = True
    game_state.ending_reached = ending_id
    game_state.save()

    # Unlock ending achievement
    unlock_ending(request, ending)

    # Get all endings for progress display
    all_endings = Ending.objects.all()
    unlocked_endings = get_unlocked_endings(request)

    context = {
        'ending': ending,
        'game_state': game_state,
        'all_endings': all_endings,
        'unlocked_endings': unlocked_endings,
    }
    return render(request, 'castle_adventure/ending.html', context)

def unlock_ending(request, ending):
    """Record ending unlock for user/session."""
    if request.user.is_authenticated:
        EndingUnlock.objects.get_or_create(
            user=request.user,
            ending=ending
        )
    else:
        EndingUnlock.objects.get_or_create(
            session_key=request.session.session_key,
            ending=ending
        )

def get_unlocked_endings(request):
    """Get list of endings this user/session has unlocked."""
    if request.user.is_authenticated:
        return EndingUnlock.objects.filter(user=request.user).values_list('ending_id', flat=True)
    else:
        return EndingUnlock.objects.filter(session_key=request.session.session_key).values_list('ending_id', flat=True)
```

### 3. Endings Collection View
```python
def endings_collection(request):
    """Display all endings with locked/unlocked status."""
    all_endings = Ending.objects.all().order_by('ending_id')
    unlocked = get_unlocked_endings(request)

    for ending in all_endings:
        ending.is_unlocked = ending.ending_id in unlocked

    context = {
        'endings': all_endings,
        'total_endings': all_endings.count(),
        'unlocked_count': len(unlocked),
    }
    return render(request, 'castle_adventure/endings_collection.html', context)
```

---

## Definition of Done

- [ ] determine_ending() logic implemented for all 5 endings
- [ ] Ending determination follows priority order (E5 → E4 → E3 → E2 → E1)
- [ ] Ending unlock tracking works for users and sessions
- [ ] display_ending view shows correct ending
- [ ] endings_collection view shows progress
- [ ] Game marked as complete when ending reached
- [ ] At least 18 tests written and passing (>95% coverage)
- [ ] Code committed with "feat(endings): implement ending determination and unlock system"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 18 tests:**
1-5. determine_ending (each ending E1-E5 triggered correctly)
6-8. Ending requirements (item checks, flag checks, NPC relations)
9-10. unlock_ending (user-based, session-based)
11-12. get_unlocked_endings (returns correct list)
13-14. display_ending (shows correct ending, marks game complete)
15-16. endings_collection (shows all, locked/unlocked status)
17-18. Integration (playthrough to ending, achievement unlock)

---

## Dependencies

- **Blocks:** T-007 (needs ending content)
- **Depends on:** T-002 (Ending model), T-003 (view structure)

---

**Created:** 2025-10-02
**Status:** Ready for Development
