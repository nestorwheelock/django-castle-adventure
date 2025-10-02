# S-004: Save and Load Game State

**Story Type**: User Story
**Priority**: High
**Estimate**: 1 day
**Sprint**: Sprint 2
**Status**: ✅ Planned (awaiting approval)

---

## User Story

**As a** player
**I want to** save my game progress and return later
**So that** I don't have to complete the adventure in one sitting

---

## Acceptance Criteria

- [ ] When I make a choice, my progress is automatically saved
- [ ] When I return to the game, I can continue from where I left off
- [ ] When I load a saved game, my current scene is restored
- [ ] When I load a saved game, my inventory is restored
- [ ] When I load a saved game, my visited scenes and flags are restored
- [ ] When I start a new game, my old save is overwritten (with confirmation)
- [ ] When I have multiple save slots, I can choose which to load

---

## Definition of Done

- [ ] GameState model implemented with all necessary fields (15 tests)
- [ ] Auto-save functionality on every choice
- [ ] Load game functionality restores complete state
- [ ] Save system handles user authentication (if logged in)
- [ ] Save system handles anonymous users (session-based)
- [ ] Multiple save slots supported (optional for v1.0)
- [ ] Tests written and passing (>95% coverage)
- [ ] Code committed with reference to this story

---

## Database Model

**GameState Model:**
```python
class GameState(models.Model):
    # User identification
    user = models.ForeignKey(User, null=True, blank=True)  # Logged-in users
    session_key = models.CharField(max_length=40, null=True)  # Anonymous users

    # Game progress
    current_scene = models.ForeignKey(Scene, related_name='active_games')
    inventory = models.JSONField(default=list)  # ["ITEM_001", "ITEM_003"]
    visited_scenes = models.JSONField(default=list)  # ["01", "02", "03"]

    # Game flags (for complex story branching)
    flags = models.JSONField(default=dict)  # {"dragon_befriended": True, "troll_killed": False}

    # Metadata
    game_started = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    ending_reached = models.CharField(max_length=10, null=True)  # "E1", "E2", etc.

    # Stats (optional)
    choices_made = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    items_collected = models.IntegerField(default=0)
```

---

## Save System Logic

**Auto-Save Triggers:**
- After every choice made
- After every item picked up
- Before entering new scene
- On game over / ending reached

**Save Strategy:**
```python
def save_game_state(game_state):
    """Auto-save after every action."""
    game_state.last_updated = timezone.now()
    game_state.save()
    return True
```

**Load Strategy:**
```python
def load_game_state(user=None, session_key=None):
    """Load most recent save for user or session."""
    if user and user.is_authenticated:
        return GameState.objects.filter(user=user).latest('last_updated')
    elif session_key:
        return GameState.objects.filter(session_key=session_key).latest('last_updated')
    return None
```

---

## State Management

**Game Flags (for story branching):**
```python
flags = {
    "dragon_befriended": False,      # Used cheese/mice strategy
    "dragon_woken": False,            # Woke dragon violently
    "troll_killed": False,            # Attacked troll
    "troll_bribed": False,            # Used goblet instead of riddle
    "wizard_pizza_played": False,     # Played along with wizard confusion
    "npc_relations": 0,               # Sum of NPC interactions (-3 to +5)
    "chaos_level": 0,                 # Destruction counter (for E4 ending)
    "sat_on_throne": False,           # Secret ending trigger
}
```

**How Flags Affect Endings:**
- E1 (Heroic Rescue): npc_relations > 0, chaos_level < 3
- E2 (Tragic Betrayal): npc_relations < 0 or killed NPCs
- E3 (Mutual Escape): dragon_befriended, troll_befriended, wizard_pizza_played
- E4 (Castle Collapse): chaos_level > 10
- E5 (New Ruler): all items + all NPCs befriended + sat_on_throne

---

## API Endpoints

**Required Views:**
- `/save/` - Manually save game (auto-save is automatic)
- `/load/` - Load most recent save
- `/saves/` - List all saves for user (if multiple slots)
- `/new-game/` - Start new game (confirm overwrite)

---

## Testing Requirements

**Unit Tests:**
- Create new game state
- Save game state
- Load game state
- Update inventory in state
- Update flags in state
- Verify state persistence

**Integration Tests:**
- Make choice, verify auto-save
- Pick up item, verify inventory saved
- Restart browser, verify load works
- Anonymous user state persists via session
- Logged-in user state persists via user ID
- New game overwrites old save

---

## Anonymous User Handling

**Session-Based Saves:**
```python
def get_or_create_game_state(request):
    """Get game state for current user or session."""
    if request.user.is_authenticated:
        game_state, created = GameState.objects.get_or_create(
            user=request.user,
            is_complete=False,
            defaults={'current_scene': Scene.objects.get(scene_id='01')}
        )
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        game_state, created = GameState.objects.get_or_create(
            session_key=session_key,
            is_complete=False,
            defaults={'current_scene': Scene.objects.get(scene_id='01')}
        )

    return game_state
```

---

## UI Requirements

**Save Confirmation:**
```
╔═══════════════════════════════════════╗
║       GAME AUTO-SAVED                 ║
╠═══════════════════════════════════════╣
║ Progress: Scene 14 (Dragon's Cave)    ║
║ Items: 3                              ║
║ Choices Made: 12                      ║
║ Last Saved: 2 minutes ago             ║
╚═══════════════════════════════════════╝
```

**Load Game Screen:**
```
╔═══════════════════════════════════════╗
║       CONTINUE YOUR ADVENTURE?        ║
╠═══════════════════════════════════════╣
║ Current Scene: Dragon's Cave          ║
║ Items Collected: 3                    ║
║ Time Played: 8 minutes                ║
║                                       ║
║ [Continue Game]  [New Game]           ║
╚═══════════════════════════════════════╝
```

---

## Edge Cases

**Handle:**
- User starts new game while existing save exists (confirm overwrite)
- Session expires (graceful failure, start new game)
- Corrupted save data (validate on load, fallback to new game)
- Concurrent saves (use database transactions)
- Saved game references deleted scene (migration/validation)

---

## Related Stories

- Depends on: S-001 (Django module), S-002 (Scene navigation), S-003 (Inventory)
- Related: S-005 (Ending tracking requires save state)
- Related: S-007 (UI needs to show save status)

---

**Document Status:** Ready for Development
**Created:** 2025-10-02
