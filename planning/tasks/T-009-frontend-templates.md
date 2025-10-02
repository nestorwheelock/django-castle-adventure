# T-009: Frontend HTML Templates

**Related Story:** S-007 (Frontend Game Interface)
**Priority:** P0 Critical
**Estimate:** 4 hours
**Sprint:** Sprint 3
**Status:** Pending

---

## AI Coding Brief

**Role:** Frontend Developer
**Objective:** Create all HTML templates for game interface (landing, game board, inventory, endings)

**User Request:** "Create Django templates for all game screens following the wireframes in planning/wireframes/"

---

## Constraints

### Allowed File Paths
- `castle_adventure/templates/castle_adventure/` (all templates)
- `castle_adventure/templates/castle_adventure/base.html`
- `castle_adventure/templates/castle_adventure/landing.html`
- `castle_adventure/templates/castle_adventure/game_board.html`
- `castle_adventure/templates/castle_adventure/inventory.html`
- `castle_adventure/templates/castle_adventure/ending.html`
- `castle_adventure/templates/castle_adventure/endings_collection.html`

### Forbidden Paths
- No CSS yet (that's T-010)

---

## Deliverables

### 1. Base Template
```django
{# base.html #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Castle of Shadows{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'castle_adventure/css/base.css' %}">
    <link rel="stylesheet" href="{% static 'castle_adventure/css/theme.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <div class="game-container">
        {% block content %}{% endblock %}
    </div>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 2. Landing Page Template
Following `planning/wireframes/01-landing-page.txt`:
```django
{# landing.html #}
{% extends 'castle_adventure/base.html' %}

{% block content %}
<header>
    <h1>Castle of Shadows</h1>
    <p class="subtitle">A Dark Medieval Adventure</p>
</header>

<div class="ascii-art-container">
    <pre class="ascii-art">
    {# Castle exterior ASCII art #}
    </pre>
</div>

{% if saved_game %}
<div class="saved-game-panel">
    <h2>💾 Saved Game Found</h2>
    <p>Current Scene: {{ saved_game.current_scene.title }}</p>
    <p>Items Collected: {{ saved_game.items_collected }}</p>
    <p>Last Played: {{ saved_game.last_updated|timesince }} ago</p>
    <a href="{% url 'castle_adventure:load' %}" class="btn btn-primary">Continue Adventure</a>
</div>
{% endif %}

<a href="{% url 'castle_adventure:start' %}" class="btn btn-secondary">Start New Adventure</a>

<nav class="footer-links">
    <a href="{% url 'castle_adventure:endings' %}">View Endings Collection</a>
    <a href="#how-to-play">How to Play</a>
</nav>
{% endblock %}
```

### 3. Game Board Template
Following `planning/wireframes/02-main-game-screen.txt`:
```django
{# game_board.html #}
{% extends 'castle_adventure/base.html' %}

{% block content %}
<header class="game-header">
    <h1>Castle of Shadows</h1>
    <div class="controls">
        <span class="save-indicator">💾 Saved</span>
        <button class="menu-btn">☰ Menu</button>
    </div>
</header>

<div class="ascii-art-container">
    <pre class="ascii-art">{{ scene.ascii_art }}</pre>
</div>

<section class="scene-display">
    <h2>{{ scene.title }}</h2>
    <p class="scene-description">{{ scene.description|linebreaks }}</p>
</section>

<section class="choices-section">
    <h3>What do you do?</h3>
    {% for choice in choices %}
    <form method="post" action="{% url 'castle_adventure:choice' choice.id %}" class="choice-form">
        {% csrf_token %}
        <button type="submit" class="choice-btn {% if choice.is_locked %}locked{% endif %}" {% if choice.is_locked %}disabled{% endif %}>
            [{{ choice.choice_letter }}] {{ choice.choice_text }}
            {% if choice.is_locked %}🔒{% endif %}
        </button>
    </form>
    {% endfor %}
</section>

<aside class="inventory-bar">
    <h4>Inventory ({{ game_state.items_collected }} items)</h4>
    <div class="inventory-preview">
        {% for item_id in game_state.inventory %}
        <span class="item-icon" title="{{ item_id }}">{{ item_id }}</span>
        {% endfor %}
    </div>
    <a href="{% url 'castle_adventure:inventory' %}">View Full</a>
</aside>

<footer class="progress-bar">
    <span>Scene {{ scene.scene_id }}</span>
    <span>Choices Made: {{ game_state.choices_made }}</span>
    <span>Items: {{ game_state.items_collected }}/8</span>
</footer>
{% endblock %}
```

### 4. Inventory Template
Following `planning/wireframes/03-inventory-view.txt`

### 5. Ending Template
Following `planning/wireframes/04-ending-screen.txt`

### 6. Endings Collection Template
Grid view of all endings with locked/unlocked status

---

## Definition of Done

- [ ] All 6 templates created
- [ ] Templates follow wireframe designs
- [ ] All Django template tags correct
- [ ] CSRF tokens on all forms
- [ ] Semantic HTML (proper heading hierarchy)
- [ ] Accessibility attributes (ARIA labels)
- [ ] Mobile-friendly viewport meta tag
- [ ] At least 8 template rendering tests passing
- [ ] Code committed with "feat(templates): implement all game interface templates"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 8 tests:**
1-2. Landing page (renders, shows saved game if exists)
3-4. Game board (renders scene, shows choices)
5. Inventory (displays items)
6-7. Ending (displays ending text, shows achievement)
8. Endings collection (shows all endings)

---

## Dependencies

- **Blocks:** T-010 (CSS needs templates to style)
- **Depends on:** T-003 (views), T-007 (content)

---

**Created:** 2025-10-02
**Status:** Ready for Development
