# T-003: Scene Navigation Views and URL Routing

**Related Story:** S-002 (Story Navigation System)
**Priority:** P0 Critical
**Estimate:** 3 hours
**Sprint:** Sprint 1
**Status:** Pending

---

## AI Coding Brief

**Role:** Backend Django Developer
**Objective:** Implement views for scene display, choice selection, and story graph navigation

**User Request:** "Create Django views for displaying scenes, making choices, and navigating the story graph"

---

## Constraints

### Allowed File Paths
- `castle_adventure/views.py`
- `castle_adventure/urls.py`
- `castle_adventure/tests/test_views.py`
- `castle_adventure/tests/test_integration.py`

### Forbidden Paths
- No templates yet (that's T-012)
- No content data yet (that's T-010)

---

## Deliverables

### 1. URL Routing
```python
# urls.py
from django.urls import path
from . import views

app_name = 'castle_adventure'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('start/', views.start_game, name='start'),
    path('scene/<str:scene_id>/', views.display_scene, name='scene'),
    path('choice/<int:choice_id>/', views.make_choice, name='choice'),
    path('inventory/', views.view_inventory, name='inventory'),
    path('save/', views.save_game, name='save'),
    path('load/', views.load_game, name='load'),
]
```

### 2. Core Views

**start_game view:**
```python
def start_game(request):
    """Start new game or load existing save."""
    game_state = get_or_create_game_state(request)
    if not game_state:
        # Create new game at Scene 01
        start_scene = Scene.objects.get(scene_id='01')
        game_state = GameState.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key,
            current_scene=start_scene
        )
    return redirect('castle_adventure:scene', scene_id=game_state.current_scene.scene_id)
```

**display_scene view:**
```python
def display_scene(request, scene_id):
    """Display current scene with choices."""
    game_state = get_game_state(request)
    scene = get_object_or_404(Scene, scene_id=scene_id)

    # Get available choices
    choices = scene.choices_from.all()

    # Filter locked choices (item requirements)
    for choice in choices:
        if choice.requires_item:
            choice.is_locked = not game_state.has_item(choice.requires_item.item_id)
        else:
            choice.is_locked = False

    # Check for items in this scene
    items_here = scene.items_here.filter(
        item_id__nin=game_state.inventory
    )

    context = {
        'scene': scene,
        'choices': choices,
        'items_here': items_here,
        'game_state': game_state,
    }
    return render(request, 'castle_adventure/game_board.html', context)
```

**make_choice view:**
```python
def make_choice(request, choice_id):
    """Process player choice and navigate to next scene."""
    game_state = get_game_state(request)
    choice = get_object_or_404(Choice, id=choice_id)

    # Validate choice is from current scene
    if choice.from_scene != game_state.current_scene:
        return HttpResponseBadRequest("Invalid choice for current scene")

    # Validate item requirements
    if choice.requires_item and not game_state.has_item(choice.requires_item.item_id):
        return HttpResponseBadRequest("Missing required item")

    # Update game state
    game_state.current_scene = choice.to_scene
    game_state.choices_made += 1
    game_state.visited_scenes.append(choice.to_scene.scene_id)

    # Check if death scene
    if choice.to_scene.is_death:
        game_state.deaths += 1

    game_state.save()

    return redirect('castle_adventure:scene', scene_id=choice.to_scene.scene_id)
```

### 3. Helper Functions
```python
def get_or_create_game_state(request):
    """Get existing game state or return None for new game."""
    if request.user.is_authenticated:
        return GameState.objects.filter(
            user=request.user,
            is_complete=False
        ).first()
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        return GameState.objects.filter(
            session_key=session_key,
            is_complete=False
        ).first()

def get_game_state(request):
    """Get current game state, raise 404 if not found."""
    state = get_or_create_game_state(request)
    if not state:
        raise Http404("No active game found")
    return state
```

---

## Definition of Done

- [ ] All URL routes defined and working
- [ ] start_game view creates new game state
- [ ] display_scene view shows scene with choices
- [ ] make_choice view navigates to next scene
- [ ] Item requirements validated before allowing choice
- [ ] Game state updated on each choice
- [ ] Helper functions for state management
- [ ] At least 15 tests written and passing (>95% coverage)
- [ ] Integration test: full scene navigation flow works
- [ ] Code committed with "feat(views): implement scene navigation and choice handling"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 15 tests:**
1-3. start_game (new game, existing save, session vs user)
4-6. display_scene (shows scene, shows choices, filters locked choices)
7-10. make_choice (valid choice, invalid choice, item requirement, state update)
11-12. Helper functions (get_or_create, get_game_state)
13-15. Integration tests (start → scene → choice → next scene)

---

## Dependencies

- **Blocks:** T-010 (content needs navigation working), T-012 (templates need views)
- **Depends on:** T-002 (models must exist)

---

**Created:** 2025-10-02
**Status:** Ready for Development
