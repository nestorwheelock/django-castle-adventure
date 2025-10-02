# Castle of Shadows (SPEC Phase - Awaiting Approval)

⚠️ **STATUS**: This project is in SPEC phase. No code has been written yet.
This README guides you through the approval process.

---

## What This Will Be

**Castle of Shadows** is a dark-humorous, 80s-style text adventure game built as a portable Django module. Players navigate a mysterious castle, solving puzzles, collecting items, and making choices that significantly alter the story. The game features ASCII art visualizations, a save system, and multiple endings based on player decisions.

**Inspired by classic 80s text adventures** with a modern web framework, this project captures the nostalgia of games like Castle Adventure, Zork, and Colossal Cave Adventure—but with a darkly comedic twist.

---

## Key Features (v1.0.0)

### Story & Content
- **25-30 interactive scenes** with atmospheric descriptions
- **5 distinct endings** based on player choices
- **Dark humor tone** - Death is frequent but comedic
- **9 unique NPCs** with personality quirks (anxious dragon, polite troll, confused wizard)
- **8 collectible items** that unlock story paths
- **5 puzzles** requiring logic and item combinations

### Gameplay
- **Story-focused adventure** - No stats or combat (v1.0)
- **Branching narrative** - Choices significantly affect story
- **Item-based puzzles** - Magic spectacles reveal invisible ink, dragon's flame melts ice, etc.
- **Multiple playthroughs** - Discover all endings and paths
- **Save/load system** - Continue your adventure later

### Technical
- **Portable Django app module** - Easy integration into any Django project
- **ASCII art visualizations** - Classic terminal aesthetic
- **Responsive UI** - Works on desktop, tablet, and mobile
- **Test-driven development** - >95% test coverage
- **Accessibility** - Keyboard navigation, screen reader support

---

## SPEC Documents for Review

Please review these planning documents before approval:

### Core Planning
- **[Project Charter](planning/PROJECT_CHARTER.md)** - What, Why, How, Success Criteria, Risks
- **[SPEC Summary](planning/SPEC_SUMMARY.md)** - Quick reference for busy reviewers

### Story Planning
- **[Story Map Overview](planning/story-map/README.md)** - World, tone, design patterns
- **[Story Graph](planning/story-map/story-graph.md)** - Complete scene map (28 scenes)
- **[Endings Guide](planning/story-map/endings.md)** - All 5 endings detailed
- **[Content Inventory](planning/story-map/content-inventory.md)** - Items, NPCs, puzzles

### User Stories
- **[S-001: Portable Django Module](planning/stories/S-001-portable-django-module.md)**
- **[S-002: Story Navigation System](planning/stories/S-002-story-navigation-system.md)**
- **[S-003: Inventory System](planning/stories/S-003-inventory-system.md)**
- **[S-004: Save/Load System](planning/stories/S-004-save-load-system.md)**
- **[S-005: Multiple Endings System](planning/stories/S-005-multiple-endings-system.md)**
- **[S-006: Story Content Implementation](planning/stories/S-006-story-content-implementation.md)**
- **[S-007: Frontend Game Interface](planning/stories/S-007-frontend-game-interface.md)**

### Visual Design
- **[Wireframes Overview](planning/wireframes/README.md)** - UI design patterns
- **[Landing Page](planning/wireframes/01-landing-page.txt)** - Game start screen
- **[Main Game Screen](planning/wireframes/02-main-game-screen.txt)** - Scene/choices interface
- **[Inventory View](planning/wireframes/03-inventory-view.txt)** - Item management
- **[Ending Screen](planning/wireframes/04-ending-screen.txt)** - Victory/defeat display

---

## Approval Process

### Step 1: Review SPEC Documents
Read through the documents above to understand:
- What will be built (scope)
- How it will work (technical approach)
- What the UI will look like (wireframes)
- What the story will be (story map)

### Step 2: Ask Questions
If anything is unclear, create comments in **GitHub Issue #1** (Approval Issue):
- What features are confusing?
- What scope needs clarification?
- What risks concern you?

### Step 3: Approve or Request Changes
Once you've reviewed everything:
- ✅ **Approve**: Close Issue #1 to formally approve and begin BUILD phase
- 📝 **Request Changes**: Comment on Issue #1 with requested modifications
- ❌ **Reject**: Close Issue #1 with "Rejected" label and explanation

---

## What Happens After Approval

Once you close Issue #1 (approval):
1. **Scope is locked** - No new features without new approval
2. **Development begins** - Following 23-step TDD cycle from CLAUDE.md
3. **This README is replaced** - Production docs will replace this approval guide
4. **GitHub issues created** - All T-XXX tasks become trackable issues
5. **Estimated timeline**: 12-18 hours for v1.0.0 (AI-assisted development)

---

## Scope Boundaries (What's IN and OUT)

### ✅ IN SCOPE for v1.0.0
- 25-30 scenes with complete story
- 5 endings (3 primary + 2 bonus)
- Inventory system (8 items)
- Save/load functionality
- ASCII art for major scenes
- Story-focused gameplay (no stats/combat)
- Single-player only
- Portable Django module
- Dark humor tone
- Responsive web interface

### ❌ OUT OF SCOPE (Future Versions)
- **v2.0.0**: More scenes (40+), more endings (7+), hint system
- **v3.0.0**: Character stats, combat system, RPG elements
- **v4.0.0**: Multiplayer, co-op puzzles, leaderboards
- Sound effects, music, animations
- Mobile app version
- Achievements beyond ending unlocks

---

## Questions?

Add comments to **GitHub Issue #1** or contact nwheelo.

---

## Technical Requirements (For Reviewers)

**Dependencies:**
- Python 3.10+
- Django 4.2+
- Modern web browser (Chrome, Firefox, Safari, Edge)

**Installation (after approval):**
```bash
pip install django-castle-adventure
```

**Integration:**
```python
# settings.py
INSTALLED_APPS = [
    ...
    'castle_adventure',
]

# urls.py
urlpatterns = [
    path('castle/', include('castle_adventure.urls')),
]
```

---

## Approval Checklist

Before approving, confirm:
- [ ] I understand what features will be in v1.0.0
- [ ] I understand what features are deferred to future versions
- [ ] I've reviewed the wireframes and understand the UI
- [ ] I've read the story map and understand the tone/content
- [ ] I've reviewed the user stories and acceptance criteria
- [ ] I understand the technical approach
- [ ] I've read the risks and mitigations
- [ ] I'm ready to lock this scope and proceed to BUILD phase

**To approve**: Close GitHub Issue #1 with comment "Approved"

---

**Document Status:** Ready for Client Review
**Created:** 2025-10-02
**Phase:** SPEC → Awaiting CLIENT APPROVAL GATE #1
