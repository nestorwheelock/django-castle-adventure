# T-004: Inventory System Implementation

**Related Story:** S-003 (Inventory System)
**Priority:** P0 Critical
**Estimate:** 2 hours
**Sprint:** Sprint 1
**Status:** Pending

---

## AI Coding Brief

**Role:** Backend Django Developer
**Objective:** Implement item pickup, inventory management, and item requirement validation

**User Request:** "Create views and logic for picking up items, displaying inventory, and validating item requirements for choices"

---

## Constraints

### Allowed File Paths
- `castle_adventure/views.py` (add to existing)
- `castle_adventure/tests/test_inventory.py`

### Forbidden Paths
- No content data yet (items defined in T-010)

---

## Deliverables

### 1. Item Pickup View
```python
def pickup_item(request, item_id):
    """Pick up an item and add to inventory."""
    game_state = get_game_state(request)
    item = get_object_or_404(Item, item_id=item_id)

    # Validate item is in current scene
    if item.found_in_scene != game_state.current_scene:
        return HttpResponseBadRequest("Item not in this scene")

    # Add to inventory
    game_state.add_item(item_id)

    return JsonResponse({
        'success': True,
        'item': {
            'id': item.item_id,
            'name': item.name,
            'description': item.description,
            'icon': item.icon,
        }
    })
```

### 2. View Inventory
```python
def view_inventory(request):
    """Display all items in inventory."""
    game_state = get_game_state(request)
    items = Item.objects.filter(item_id__in=game_state.inventory)

    context = {
        'items': items,
        'game_state': game_state,
    }
    return render(request, 'castle_adventure/inventory.html', context)
```

### 3. Item Requirement Validation
Already implemented in T-003's make_choice view, but add comprehensive tests.

---

## Definition of Done

- [ ] pickup_item view implemented
- [ ] view_inventory view implemented
- [ ] Item pickup updates GameState.inventory
- [ ] Item pickup increments items_collected counter
- [ ] Cannot pick up same item twice
- [ ] Cannot pick up item from wrong scene
- [ ] Item requirements validated in choice selection
- [ ] At least 12 tests written and passing (>95% coverage)
- [ ] Code committed with "feat(inventory): implement item pickup and inventory management"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 12 tests:**
1-3. pickup_item (valid pickup, duplicate prevention, wrong scene)
4-5. view_inventory (empty, with items)
6-8. GameState.add_item (adds to inventory, increments counter, prevents duplicates)
9-10. GameState.has_item (returns true/false correctly)
11-12. Integration (pickup item, use in choice requirement)

---

## Dependencies

- **Blocks:** T-010 (content needs inventory working)
- **Depends on:** T-002 (Item model), T-003 (view structure)

---

**Created:** 2025-10-02
**Status:** Ready for Development
