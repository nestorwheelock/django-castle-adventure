# S-005: Multiple Endings System

**Story Type**: User Story
**Priority**: Medium
**Estimate**: 1 day
**Sprint**: Sprint 2
**Status**: ✅ Planned (awaiting approval)

---

## User Story

**As a** player
**I want to** reach different endings based on my choices
**So that** I can replay the game and discover new outcomes

---

## Acceptance Criteria

- [ ] When I complete the game, I reach one of 5 possible endings
- [ ] When I reach an ending, I see which ending I got
- [ ] When I view my profile, I see which endings I've unlocked
- [ ] When I replay, I can discover different endings by making different choices
- [ ] When I unlock all endings, I get a completion achievement
- [ ] When the game determines my ending, it uses my items, choices, and flags

---

## Definition of Done

- [ ] Ending model implemented with ending logic (10 tests)
- [ ] Ending determination algorithm implemented
- [ ] All 5 endings from endings.md implemented
- [ ] Ending unlock tracking per user
- [ ] Ending display with full text and achievement
- [ ] Replay encouragement for undiscovered endings
- [ ] Tests written and passing (>95% coverage)
- [ ] Code committed with reference to this story

---

## Endings to Implement (5 Total)

**E1: Heroic Rescue** ⭐ (Primary Victory)
- **Requirements:** Tower Key, Dragon's Flame, Magic Spectacles, helped NPCs
- **Trigger:** npc_relations > 0, chaos_level < 3
- **Type:** Victory

**E2: Tragic Betrayal** 🗡️ (Dark Twist)
- **Requirements:** Reached princess without helping NPCs OR killed NPCs
- **Trigger:** npc_relations < 0 or killed_npcs flag
- **Type:** Death/Betrayal

**E3: Mutual Escape** 🤝 (Partnership Victory)
- **Requirements:** Royal Seal, befriended all NPCs
- **Trigger:** dragon_befriended, troll_befriended, wizard_helped, Royal Seal in inventory
- **Type:** Victory

**E4: Castle Collapse** 💥 (Chaotic Comedy)
- **Requirements:** High chaos level from destruction
- **Trigger:** chaos_level > 10
- **Type:** Comedy Victory

**E5: Become the New Ruler** 👑 (Secret Ending)
- **Requirements:** ALL items, ALL NPCs befriended, sat on throne
- **Trigger:** len(inventory) == 7, all_npcs_befriended, sat_on_throne flag
- **Type:** Secret

---

## Database Model

**Ending Model:**
```python
class Ending(models.Model):
    ending_id = models.CharField(max_length=10, unique=True)  # "E1", "E2", etc.
    title = models.CharField(max_length=200)
    description = models.TextField()
    ending_type = models.CharField(max_length=20)  # victory/betrayal/comedy/secret
    icon = models.CharField(max_length=10)  # "⭐", "🗡️", "🤝", etc.
    achievement_text = models.CharField(max_length=200)
    is_secret = models.BooleanField(default=False)

    # Requirements for this ending (stored as JSON for flexibility)
    requirements = models.JSONField(default=dict)
    # Example: {"items": ["ITEM_001", "ITEM_002"], "flags": {"npc_relations": ">0"}}
```

**EndingUnlock Model (tracks which endings player has seen):**
```python
class EndingUnlock(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True)
    ending = models.ForeignKey(Ending)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'ending'], ['session_key', 'ending']]
```

---

## Ending Determination Algorithm

```python
def determine_ending(game_state):
    """
    Determine which ending the player reaches based on game state.
    Check in order of specificity (most specific first).
    """
    items = game_state.inventory
    flags = game_state.flags

    # E5: Secret Ending (most specific)
    if (len(items) == 7 and
        flags.get('dragon_befriended') and
        flags.get('troll_befriended') and
        flags.get('wizard_helped') and
        flags.get('sat_on_throne')):
        return 'E5'

    # E4: Castle Collapse (high chaos)
    if flags.get('chaos_level', 0) > 10:
        return 'E4'

    # E3: Mutual Escape (partnership)
    if ('ITEM_004' in items and  # Royal Seal
        flags.get('dragon_befriended') and
        flags.get('troll_befriended') and
        flags.get('wizard_helped')):
        return 'E3'

    # E2: Tragic Betrayal (negative relations)
    if flags.get('npc_relations', 0) < 0 or flags.get('killed_npcs'):
        return 'E2'

    # E1: Heroic Rescue (default victory)
    if ('ITEM_001' in items and  # Spectacles
        'ITEM_002' in items and  # Dragon's Flame
        'ITEM_003' in items):    # Tower Key
        return 'E1'

    # Fallback (shouldn't reach this if game is complete)
    return 'E1'
```

---

## Flag Updates During Game

**Examples of flag updates:**

**Dragon Interaction:**
```python
# Peaceful cheese/mice strategy
if player_uses_cheese:
    game_state.flags['dragon_befriended'] = True
    game_state.flags['npc_relations'] += 1

# Violent wake-up
elif player_wakes_dragon_violently:
    game_state.flags['dragon_woken'] = True
    game_state.flags['chaos_level'] += 3
```

**Troll Interaction:**
```python
# Answered riddle correctly
if riddle_correct:
    game_state.flags['troll_befriended'] = True
    game_state.flags['npc_relations'] += 1

# Attacked troll
elif player_attacks:
    game_state.flags['killed_npcs'] = True
    game_state.flags['npc_relations'] -= 2
    game_state.flags['chaos_level'] += 2
```

**Destruction Actions:**
```python
# Breaking things increases chaos
if action in ['fight_armor', 'break_door', 'destroy_furniture']:
    game_state.flags['chaos_level'] += 1
```

---

## API Endpoints

**Required Views:**
- `/ending/<ending_id>/` - Display ending with full text and achievement
- `/endings/` - View all endings (locked/unlocked status)
- `/achievement/<ending_id>/` - Unlock achievement when ending is reached

---

## Testing Requirements

**Unit Tests:**
- Ending determination logic for each ending
- Flag updates during key interactions
- Ending unlock recording
- All endings unlocked achievement

**Integration Tests:**
- Playthrough to E1 (heroic rescue)
- Playthrough to E2 (betrayal)
- Playthrough to E3 (partnership)
- Playthrough to E4 (chaos)
- Playthrough to E5 (secret - requires all items and flags)
- Verify ending unlocks are saved
- Verify replay shows different endings

---

## UI Requirements

**Ending Display:**
```
╔═══════════════════════════════════════════════════════════════╗
║                    ⭐ HEROIC RESCUE ⭐                         ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║ [Full ending text from endings.md displayed here...]         ║
║                                                               ║
║ Princess Elara carefully evaluates you...                    ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║        ACHIEVEMENT UNLOCKED: HEROIC RESCUE                    ║
║        The classic ending. Well done!                         ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║ You have discovered 1 of 5 endings!                          ║
║                                                               ║
║ [Play Again]  [View All Endings]  [Main Menu]                ║
╚═══════════════════════════════════════════════════════════════╝
```

**Endings Collection Screen:**
```
╔═══════════════════════════════════════════════════════════════╗
║              ENDINGS DISCOVERED: 3 / 5                        ║
╠═══════════════════════════════════════════════════════════════╣
║ ⭐ Heroic Rescue          [UNLOCKED] ✅                       ║
║    The classic ending. Well done!                             ║
║                                                               ║
║ 🗡️ Tragic Betrayal       [UNLOCKED] ✅                       ║
║    Maybe read people better next time?                        ║
║                                                               ║
║ 🤝 Mutual Escape          [UNLOCKED] ✅                       ║
║    Cooperation beats solo heroics!                            ║
║                                                               ║
║ 💥 Castle Collapse        [LOCKED] 🔒                        ║
║    ???                                                        ║
║                                                               ║
║ 👑 ??? (Secret)           [LOCKED] 🔒                        ║
║    ???                                                        ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Replay Encouragement

**After Ending:**
- Show how many endings remain undiscovered
- Provide hints for how to reach other endings (without spoilers)
- Track completion percentage

**Hints System (optional for v1.0):**
- E1: "What if you helped everyone you met?"
- E2: "What if you took a more... aggressive approach?"
- E3: "What if you focused on making friends, not just collecting items?"
- E4: "What if you broke EVERYTHING?"
- E5: "What if you collected EVERYTHING and helped EVERYONE?"

---

## Related Stories

- Depends on: S-002 (Scene navigation), S-003 (Inventory), S-004 (Save state with flags)
- Related: S-006 (Story content includes ending text)
- Related: S-007 (UI displays endings and achievements)

---

**Document Status:** Ready for Development
**Created:** 2025-10-02
