# Project Charter: Django Castle Adventure

**Project Name:** django-castle-adventure
**Version:** v1.0.0 (EPOCH 1)
**Date:** 2025-10-02
**Type:** Choose-Your-Own-Adventure Django Module

---

## What We're Building

A dark-humorous, 80s-style text adventure game as a portable Django module. Players navigate a mysterious castle, solving puzzles, collecting items, and making choices that significantly alter the story. The game features ASCII art visualizations, a save system, and multiple endings based on player decisions.

**Core Experience:**
- Escape hounds across garden walls
- Drop drawbridge grate to enter castle
- Explore castle rooms (throne room, dungeon, tower, etc.)
- Discover items (keys, magic spectacles, dragon's flame)
- Solve puzzles (invisible ink clues, locked doors)
- Encounter NPCs (troll, dragon, wizard, princess)
- Reach one of 3-5 different endings

---

## Why We're Building This

**Purpose:**
1. **Test AI-assisted TDD workflow with content-heavy projects** - Validate that our disciplined development method works for story-driven applications with complex branching narratives
2. **Create engaging, replayable game experience** - Capture the nostalgia and discovery of classic 80s text adventures with modern web technology
3. **Build portable Django module** - Following pattern from tic-tac-toe and sudoku projects

**Business Value:**
- Demonstrates complex state management and branching logic
- Tests workflow's ability to handle 25-30 interconnected scenes
- Validates story planning and TDD for narrative content
- May require 3-4 epochs (multiple release cycles)

---

## How We're Building It

### Technical Approach

**Framework:** Django (portable app module)
**Pattern:** Story-focused CYOA (no stats/combat in v1.0)
**Architecture:**

```
Models:
- Scene (id, title, description, ascii_art, is_ending)
- Choice (id, from_scene, to_scene, choice_text, requires_item)
- Item (id, name, description, found_in_scene)
- GameState (user, current_scene, inventory JSON, visited_scenes, flags)
- Ending (id, scene, title, ending_type)

Views:
- Game start/continue
- Current scene display
- Make choice (validate, update state, navigate)
- Pick up item
- Save/load game state
- Game over/ending display

Frontend:
- ASCII art rendering
- Choice buttons
- Inventory display
- Save/load controls
- Atmospheric dark theme
```

**Story Graph Structure:**
- ~25-30 scenes total
- 3-5 distinct endings
- Critical path: Garden → Drawbridge → Castle → Quest → Resolution
- Branching based on items collected and choices made
- Puzzle elements require specific items to progress
- No dead-ends without narrative resolution

### Development Phases (Multi-Epoch Project)

**EPOCH 1 (v1.0.0): Core Story Engine**
- Database models and migrations
- Story graph navigation
- Inventory system
- Save/load functionality
- Main story arc (15-20 scenes)
- 3 primary endings
- Basic ASCII art

**EPOCH 2 (v2.0.0): Story Expansion** (Future)
- Additional scenes (30-40 total)
- More endings (5-7 total)
- Side quests and optional paths
- Enhanced ASCII art
- Hint system

**EPOCH 3 (v3.0.0): RPG Elements** (Future)
- Character stats (health, courage, wit)
- Simple combat system
- Resource management
- Character classes
- Achievement system

**EPOCH 4 (v4.0.0): Multiplayer** (Future)
- Shared world exploration
- Cooperative puzzle solving
- Leaderboards
- Social features

---

## Success Criteria (v1.0.0)

### Technical Success
- ✅ All automated tests pass with >95% coverage
- ✅ Story graph integrity validated (no orphaned scenes, no dead-ends except endings)
- ✅ Complete playthrough without errors
- ✅ Save/load system works reliably
- ✅ All 3+ endings reachable from START

### User Experience Success
- ✅ Engaging story with dark humor tone
- ✅ Meaningful choices that alter story progression
- ✅ Puzzle difficulty is fair (clues available through exploration)
- ✅ ASCII art enhances atmosphere and visualization
- ✅ Players want to replay to discover other endings
- ✅ Story has "aha!" moments and satisfying discoveries

### Story Content Success
- ✅ 25-30 scenes complete with descriptions
- ✅ Core story arc coherent and satisfying
- ✅ Item-based puzzles functional (spectacles reveal invisible ink, etc.)
- ✅ NPCs have personality and purpose
- ✅ Endings feel earned and distinct

### Development Process Success
- ✅ TDD workflow successfully applied to content planning
- ✅ Story planning documents prevent scope creep
- ✅ Automated tests validate story logic
- ✅ Documentation guides future story expansion

---

## Risks & Mitigations

### Risk 1: Story Branching Complexity Explosion
**Risk:** 30 scenes with 3-4 choices each = exponential paths, unmaintainable
**Probability:** HIGH
**Impact:** HIGH
**Mitigation:**
- Use "funnel" structure: branches converge back to critical path
- Limit true branching to key decision points (5-7 major forks)
- Many choices are cosmetic (different dialogue, same outcome)
- Story map planning prevents runaway branching

### Risk 2: Content Creation Slows Development
**Risk:** Writing 30 engaging scenes takes longer than coding
**Probability:** MEDIUM
**Impact:** MEDIUM
**Mitigation:**
- Start with 15-scene MVP, expand to 30 in iterations
- Content creation is part of BUILD phase tasks
- Use templates for scene structure (intro, choices, outcomes)
- Focus on main arc first, side content later

### Risk 3: TDD for Narrative Content is Unclear
**Risk:** Hard to write tests for "is the story good?"
**Probability:** MEDIUM
**Impact:** LOW
**Mitigation:**
- Test story LOGIC (graph integrity, item mechanics), not quality
- Human validation in ACCEPTANCE TEST phase
- Automated tests: reachability, no dead-ends, item requirements work
- Manual playtesting validates narrative coherence

### Risk 4: Save/Load State Management Bugs
**Risk:** Complex game state (inventory, flags, visited scenes) prone to bugs
**Probability:** MEDIUM
**Impact:** MEDIUM
**Mitigation:**
- JSON field for flexible state storage
- Comprehensive test suite for state transitions
- Save state on every choice (no data loss)
- Load state validation on game start

### Risk 5: Scope Creep During Story Writing
**Risk:** "Let's add just one more cool puzzle..." spirals out of control
**Probability:** HIGH
**Impact:** HIGH
**Mitigation:**
- **SPEC phase locks story scope** (25-30 scenes, no more)
- Story map shows exact scenes for v1.0
- Additional ideas captured for v2.0
- **CLIENT APPROVAL GATE #1 enforces scope boundaries**

---

## Scope Boundaries

### IN SCOPE (v1.0.0)

**Story Content:**
- ✅ 25-30 total scenes
- ✅ Main quest arc (find princess / escape castle / solve mystery)
- ✅ 3-5 distinct endings
- ✅ Key story locations: Garden, Drawbridge, Courtyard, Throne Room, Dungeon, Tower
- ✅ Items: Keys, Magic Spectacles, Dragon's Flame, Royal Seal (5-7 items total)
- ✅ NPCs: Hounds, Troll, Dragon, Wizard, Princess (5-7 NPCs)
- ✅ Puzzles: Invisible ink, locked doors, item combinations (3-5 puzzles)

**Features:**
- ✅ Story graph navigation
- ✅ Inventory system (collect, use, display)
- ✅ Save/load game state
- ✅ ASCII art for major scenes
- ✅ Choice validation (can't choose locked options)
- ✅ Ending tracking (which endings discovered)
- ✅ Dark humor tone and writing

**Technical:**
- ✅ Django models (Scene, Choice, Item, GameState, Ending)
- ✅ API endpoints (start, load, make_choice, save, get_state)
- ✅ Frontend templates (game board, inventory, ASCII art display)
- ✅ Test suite (>95% coverage)
- ✅ Portable Django app (pip installable)

### OUT OF SCOPE (Future Epochs)

**v2.0.0 (Story Expansion):**
- ❌ Side quests and optional areas
- ❌ More than 30 scenes
- ❌ More than 5 endings
- ❌ Hint/walkthrough system
- ❌ Achievement tracking

**v3.0.0 (RPG Elements):**
- ❌ Character stats (health, courage, wit)
- ❌ Combat system
- ❌ Resource management (food, torch fuel)
- ❌ Character classes or customization
- ❌ Skill checks (dice rolls, stat requirements)

**v4.0.0 (Multiplayer):**
- ❌ Multiple players in same world
- ❌ Cooperative puzzle solving
- ❌ Competitive modes
- ❌ Leaderboards or social features

**Polish (Not v1.0):**
- ❌ Sound effects or music
- ❌ Animated ASCII art
- ❌ Custom fonts or themes
- ❌ Mobile app version
- ❌ Speedrun timer

---

## Constraints & Assumptions

### Constraints
- Must be portable Django module (like django-sudoku, django-tictactoe)
- Story-focused only (no stats/combat in v1.0)
- Single-player only (v1.0)
- Text and ASCII art only (no images/graphics)
- Must work with standard Django versions (4.x+)

### Assumptions
- Players are familiar with text adventure conventions
- Players will read scene descriptions (not just click through)
- Save system uses Django session or database (not local storage)
- ASCII art renders correctly in monospace fonts
- Dark humor is PG-13 rated (no excessive gore/profanity)

---

## Stakeholders

**Developer:** AI-assisted development (Claude + nwheelo)
**Client:** nwheelo
**End Users:** Players who enjoy text adventures, retro games, puzzle games

---

## Timeline Estimate

**EPOCH 1 (v1.0.0):**
- SPEC Phase: 2-3 hours (story planning, user stories, wireframes)
- BUILD Phase: 8-12 hours (models, story content, frontend, tests)
- VALIDATION Phase: 1-2 hours (internal QA, playtesting)
- ACCEPTANCE TEST Phase: 1 hour (client playthrough)
- SHIP Phase: 30 minutes (deployment, documentation)

**Total: ~12-18 hours estimated for v1.0.0**

**Note:** This assumes AI-assisted development with 75-80% efficiency discount vs traditional development.

---

## Next Steps

1. ✅ Project Charter complete
2. → Create Story Map (story graph, scene list, main arc)
3. → Define User Stories with acceptance criteria
4. → Create ASCII wireframes for UI
5. → Break down into tasks (T-XXX)
6. → Get CLIENT APPROVAL GATE #1
7. → Proceed to BUILD phase

---

**Document Status:** Draft for Client Review
**Prepared By:** Claude (AI Assistant)
**Review Date:** 2025-10-02
