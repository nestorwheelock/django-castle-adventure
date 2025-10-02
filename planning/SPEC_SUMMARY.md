# SPEC Summary: Django Castle Adventure v1.0.0

**Quick Reference for Busy Reviewers**

---

## TL;DR

**What:** Dark-humorous 80s-style text adventure game as Django module
**Story:** 25-30 scenes, rescue princess from cursed castle, 5 endings
**Gameplay:** Story-focused CYOA, item-based puzzles, save system
**Timeline:** 12-18 hours (AI-assisted development)
**Risk Level:** Medium (content-heavy project, TDD for narrative)

---

## Project at a Glance

| Attribute | Value |
|-----------|-------|
| **Project Name** | django-castle-adventure |
| **Version** | v1.0.0 (EPOCH 1) |
| **Type** | Portable Django App Module |
| **Genre** | Text Adventure / CYOA |
| **Tone** | Dark Humor, 80s Retro |
| **Target Audience** | Retro game fans, puzzle enthusiasts |
| **Platform** | Web (Django) |
| **Estimated Dev Time** | 12-18 hours |
| **Test Coverage** | >95% |

---

## Core Features (v1.0.0)

### Story & Content
- ✅ **28 total scenes** (21 story + 6 deaths + 5 endings)
- ✅ **5 endings** (Heroic Rescue, Tragic Betrayal, Mutual Escape, Castle Collapse, Secret Ruler)
- ✅ **9 NPCs** with unique personalities (anxious dragon, polite troll, blind wizard, sarcastic princess)
- ✅ **8 items** (3 critical, 4 optional, 1 trap)
- ✅ **5 puzzles** (escape hounds, troll riddle, invisible ink, dragon negotiation, frozen stairs)
- ✅ **Dark humor** throughout (deaths are funny, NPCs have quirks)

### Gameplay Mechanics
- ✅ **Story navigation** - Choice-based branching narrative
- ✅ **Inventory system** - Collect and use items
- ✅ **Save/load** - Resume progress anytime
- ✅ **Multiple endings** - Replay to discover all paths
- ✅ **Item requirements** - Puzzles unlock with correct items
- ✅ **No combat/stats** - Pure story focus (v1.0)

### Technical Implementation
- ✅ **Portable Django app** - pip installable module
- ✅ **Database models** - Scene, Choice, Item, GameState, Ending
- ✅ **REST-like views** - Scene display, choice selection, save/load
- ✅ **Responsive UI** - Desktop, tablet, mobile
- ✅ **ASCII art** - Terminal-style visuals
- ✅ **Test-driven** - >95% coverage

---

## Story Overview

**The Quest:**
You must rescue Princess Elara from the cursed Castle Shadowmere. But the castle is full of deadly traps, supernatural creatures, and dark magic. Worse, the princess might be less grateful than you'd expect.

**Story Arc:**
1. **Act I: Infiltration** (8 scenes) - Escape hounds, enter castle
2. **Act II: Exploration** (10 scenes) - Solve puzzles, collect items, meet NPCs
3. **Act III: Resolution** (3 scenes + endings) - Reach tower, determine fate

**Tone Examples:**
- "The hounds appreciate your optimism if not your tactical thinking."
- Dragon: "AHHH! A human! Are you dangerous? Please don't hurt me!"
- Princess: "Oh wonderful, a rescuer. I was only three days from escaping myself."

---

## User Stories (7 Total)

| Story ID | Title | Priority | Estimate |
|----------|-------|----------|----------|
| S-001 | Portable Django Module | High | 1 day |
| S-002 | Story Navigation System | High | 2 days |
| S-003 | Inventory System | High | 1 day |
| S-004 | Save/Load System | High | 1 day |
| S-005 | Multiple Endings System | Medium | 1 day |
| S-006 | Story Content Implementation | High | 3 days |
| S-007 | Frontend Game Interface | High | 2 days |

**Total:** ~11 days (with overlap, actual: 12-18 hours AI-assisted)

---

## Technical Architecture

### Database Models
```python
Scene(scene_id, title, description, ascii_art, is_ending, is_death)
Choice(from_scene, to_scene, choice_text, requires_item)
Item(item_id, name, description, found_in_scene)
GameState(user/session, current_scene, inventory, flags)
Ending(ending_id, title, description, requirements)
```

### Story Graph Structure
- **Funnel branching** - Paths converge to prevent explosion
- **3 convergence points** - Scenes 07, 09, 19
- **Critical path** - 15 scenes from START to ending
- **Graph validation** - No orphans, no dead-ends (except deaths/endings)

---

## Scope Boundaries

### ✅ IN v1.0.0
- 25-30 scenes
- 5 endings
- Item-based puzzles
- Save/load
- ASCII art
- Story-focused (no combat)

### ❌ OUT (Future)
- More scenes/endings
- Character stats/combat
- Multiplayer
- Sound/music
- Mobile app

---

## Key Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Story branching complexity** | HIGH | HIGH | Funnel structure, convergence points |
| **Content creation slowdown** | MEDIUM | MEDIUM | Phased content (MVP → full) |
| **TDD for narrative** | MEDIUM | LOW | Test logic not quality, human validation |
| **Scope creep** | HIGH | HIGH | **SPEC locks scope, client approval gate** |
| **Save state bugs** | MEDIUM | MEDIUM | Comprehensive state tests, JSON validation |

---

## Success Criteria

### Technical Success
- ✅ All tests pass (>95% coverage)
- ✅ Story graph validated (no orphans/dead-ends)
- ✅ Complete playthrough without errors
- ✅ Save/load works reliably
- ✅ All 5 endings reachable

### User Experience Success
- ✅ Engaging story with dark humor
- ✅ Meaningful choices that alter progression
- ✅ Fair puzzles with available clues
- ✅ ASCII art enhances atmosphere
- ✅ Players want to replay

### Story Content Success
- ✅ 25-30 scenes complete
- ✅ Core arc coherent
- ✅ Item puzzles functional
- ✅ NPCs have personality
- ✅ Endings feel earned

---

## Timeline & Phases

### SPEC Phase (CURRENT)
- ✅ Requirements gathered
- ✅ Story map created
- ✅ User stories defined
- ✅ Wireframes completed
- ⏳ **Awaiting client approval**

### BUILD Phase (After Approval)
- Sprint 1: Django module, navigation, inventory (3 days)
- Sprint 2: Save system, endings, core content (4 days)
- Sprint 3: Frontend, full content, polish (4 days)

### VALIDATION Phase
- Internal QA, playtesting (1 day)

### ACCEPTANCE TEST Phase
- Client playthrough, feedback (1 day)

### SHIP Phase
- Deploy, document, release (0.5 days)

---

## Approval Decision Points

### Approve if:
- ✅ Scope is clear and achievable
- ✅ Story tone matches expectations
- ✅ Technical approach is sound
- ✅ Wireframes show acceptable UX
- ✅ Risks are manageable

### Request changes if:
- 📝 Scope is unclear or too large/small
- 📝 Story content needs adjustment
- 📝 Technical approach has concerns
- 📝 UI needs modification

### Reject if:
- ❌ Fundamental disagreement on direction
- ❌ Resources/timeline unacceptable
- ❌ Risks too high

---

## Next Steps After Approval

1. **Scope lock** - No changes without new approval
2. **Create GitHub issues** - All T-XXX tasks tracked
3. **Begin BUILD** - Follow 23-step TDD cycle
4. **Replace README** - Production docs replace approval guide
5. **Estimated delivery** - 12-18 hours of development

---

## Questions for Client

1. **Story tone**: Is dark humor (comedic deaths, quirky NPCs) appropriate?
2. **Scope size**: Is 25-30 scenes the right size for v1.0, or adjust?
3. **ASCII art**: Is terminal-style ASCII acceptable, or prefer images?
4. **Save system**: Anonymous session-based saves OK, or require login?
5. **Future plans**: Interest in v2.0 (more content) or v3.0 (RPG elements)?

---

## Approval

**To approve this SPEC:**
- Close GitHub Issue #1 with comment "Approved"

**To request changes:**
- Comment on Issue #1 with requested modifications

**To reject:**
- Close Issue #1 with "Rejected" label and explanation

---

**Document Status:** Ready for Approval
**Created:** 2025-10-02
**Phase:** SPEC → CLIENT APPROVAL GATE #1
