from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, Http404, JsonResponse
from .models import Scene, Choice, Item, GameState


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


def landing_page(request):
    """Landing page for the game."""
    return render(request, 'castle_adventure/landing.html')


def start_game(request):
    """Start new game or load existing save."""
    game_state = get_or_create_game_state(request)
    if not game_state:
        start_scene = Scene.objects.get(scene_id='01')
        game_state = GameState.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key if not request.user.is_authenticated else None,
            current_scene=start_scene
        )
    return redirect('castle_adventure:scene', scene_id=game_state.current_scene.scene_id)


def display_scene(request, scene_id):
    """Display current scene with choices."""
    game_state = get_game_state(request)
    scene = get_object_or_404(Scene, scene_id=scene_id)

    choices = scene.choices_from.all()

    for choice in choices:
        if choice.requires_item:
            choice.is_locked = not game_state.has_item(choice.requires_item.item_id)
        else:
            choice.is_locked = False

    items_here = scene.items_here.exclude(item_id__in=game_state.inventory)

    context = {
        'scene': scene,
        'choices': choices,
        'items_here': items_here,
        'game_state': game_state,
    }
    return render(request, 'castle_adventure/game_board.html', context)


def make_choice(request, choice_id):
    """Process player choice and navigate to next scene."""
    game_state = get_game_state(request)
    choice = get_object_or_404(Choice, id=choice_id)

    if choice.from_scene != game_state.current_scene:
        return HttpResponseBadRequest("Invalid choice for current scene")

    if choice.requires_item and not game_state.has_item(choice.requires_item.item_id):
        return HttpResponseBadRequest("Missing required item")

    game_state.current_scene = choice.to_scene
    game_state.choices_made += 1

    if choice.to_scene.scene_id not in game_state.visited_scenes:
        game_state.visited_scenes.append(choice.to_scene.scene_id)

    if choice.to_scene.is_death:
        game_state.deaths += 1

    game_state.save()

    return redirect('castle_adventure:scene', scene_id=choice.to_scene.scene_id)


def pickup_item(request, item_id):
    """Pick up an item and add to inventory."""
    game_state = get_game_state(request)
    item = get_object_or_404(Item, item_id=item_id)

    if item.found_in_scene != game_state.current_scene:
        return HttpResponseBadRequest("Item not in this scene")

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


def view_inventory(request):
    """View player inventory."""
    game_state = get_game_state(request)
    items = Item.objects.filter(item_id__in=game_state.inventory)

    context = {
        'game_state': game_state,
        'items': items,
    }
    return render(request, 'castle_adventure/inventory.html', context)


def save_game(request):
    """Save current game state."""
    game_state = get_game_state(request)
    return render(request, 'castle_adventure/save_game.html', {'game_state': game_state})


def load_game(request):
    """Load saved game state."""
    game_state = get_or_create_game_state(request)
    if game_state:
        return redirect('castle_adventure:scene', scene_id=game_state.current_scene.scene_id)
    return redirect('castle_adventure:start')
