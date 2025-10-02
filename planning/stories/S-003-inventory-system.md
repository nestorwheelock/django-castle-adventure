# S-003: Inventory System

**Story Type**: User Story
**Priority**: High
**Estimate**: 1 day
**Sprint**: Sprint 1
**Status**: ✅ Planned (awaiting approval)

---

## User Story

**As a** player
**I want to** collect and use items during my adventure
**So that** I can solve puzzles and unlock new story paths

---

## Acceptance Criteria

- [ ] When I enter a scene with an item, I see a prompt to pick it up
- [ ] When I pick up an item, it is added to my inventory
- [ ] When I view my inventory, I see all collected items with descriptions
- [ ] When I try to make a choice that requires an item, the system checks my inventory
- [ ] When I have the required item, I can make that choice
- [ ] When I lack the required item, the choice is locked or disabled
- [ ] When I use an item (if consumable), it is removed from inventory

---

## Definition of Done

- [ ] Item model implemented with name, description, found_in_scene fields (12 tests)
- [ ] Inventory stored in GameState model (JSON field or ManyToMany)
- [ ] Pick up item view and logic implemented
- [ ] Item requirement validation in choice selection
- [ ] All 8 items from content-inventory.md implemented
- [ ] Inventory display in game UI
- [ ] Tests written and passing (>95% coverage)
- [ ] Code committed with reference to this story

---

## Items to Implement (8 Total)

**Critical Path Items:**
- ITEM_001: Magic Spectacles (Troll's Lair, Scene 13)
- ITEM_002: Dragon's Flame (Dragon's Cave, Scene 14)
- ITEM_003: Tower Key (Behind Throne, Scene 08)

**Optional Items:**
- ITEM_004: Royal Seal (Wizard's Study, Scene 16)
- ITEM_005: Golden Goblet (Throne Room, Scene 08)
- ITEM_006: Moldy Cheese (Kitchen, Scene 15)
- ITEM_007: Ancient Tome (Library, Scene 10)

**Trap Items:**
- ITEM_008: Rusty Sword (Armory, Scene 17 - triggers death)

---

## Database Models

**Item Model:**
```python
class Item(models.Model):
    item_id = models.CharField(max_length=20, unique=True)  # "ITEM_001"
    name = models.CharField(max_length=100)
    description = models.TextField()
    found_in_scene = models.ForeignKey(Scene, related_name='items_here')
    is_critical = models.BooleanField(default=False)
    is_consumable = models.BooleanField(default=False)
    is_trap = models.BooleanField(default=False)
```

**GameState Inventory (JSON field):**
```python
class GameState(models.Model):
    # ... other fields ...
    inventory = models.JSONField(default=list)  # ["ITEM_001", "ITEM_003"]

    def has_item(self, item_id):
        return item_id in self.inventory

    def add_item(self, item_id):
        if item_id not in self.inventory:
            self.inventory.append(item_id)
            self.save()

    def remove_item(self, item_id):
        if item_id in self.inventory:
            self.inventory.remove(item_id)
            self.save()
```

---

## Item-Based Puzzles

**Puzzle 1: Invisible Ink Message**
- **Requires:** Magic Spectacles (ITEM_001)
- **Scene:** Library (Scene 10)
- **Unlocks:** Reveals location of Tower Key

**Puzzle 2: Frozen Staircase**
- **Requires:** Dragon's Flame (ITEM_002)
- **Scene:** Tower Staircase (Scene 19)
- **Unlocks:** Access to tower and princess

**Puzzle 3: Troll's Bribe**
- **Requires:** Golden Goblet (ITEM_005) - OPTIONAL
- **Scene:** Troll's Lair (Scene 13)
- **Unlocks:** Skip riddle challenge, get spectacles

**Puzzle 4: Dragon Negotiation**
- **Requires:** Moldy Cheese (ITEM_006) - OPTIONAL
- **Scene:** Dragon's Cave (Scene 14)
- **Unlocks:** Peaceful dragon interaction

---

## API Endpoints

**Required Views:**
- `/pickup/<item_id>/` - Pick up item, add to inventory
- `/inventory/` - Display player's inventory
- `/use/<item_id>/` - Use item (if consumable)

---

## Testing Requirements

**Unit Tests:**
- Item model creation
- Add item to inventory
- Remove item from inventory
- Check if player has item
- Item requirement validation

**Integration Tests:**
- Pick up item and see it in inventory
- Use item to unlock choice
- Cannot make choice without required item
- Consumable item removed after use
- Trap item triggers correct consequence

---

## UI Requirements

**Inventory Display:**
```
╔═══════════════════════════════════════╗
║         YOUR INVENTORY                ║
╠═══════════════════════════════════════╣
║ 🔮 Magic Spectacles                   ║
║    Reveals hidden messages            ║
║                                       ║
║ 🔥 Dragon's Flame                     ║
║    Melts magical ice                  ║
║                                       ║
║ 🗝️  Tower Key                         ║
║    Opens princess's chamber           ║
╚═══════════════════════════════════════╝
```

---

## Related Stories

- Depends on: S-001 (Django module), S-002 (Scene navigation)
- Related: S-006 (Story content includes item descriptions)
- Related: S-004 (Save system must persist inventory)

---

**Document Status:** Ready for Development
**Created:** 2025-10-02
