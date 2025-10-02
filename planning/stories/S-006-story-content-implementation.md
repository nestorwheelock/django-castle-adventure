# S-006: Story Content Implementation

**Story Type**: User Story
**Priority**: High
**Estimate**: 3 days
**Sprint**: Sprint 2 & 3
**Status**: ✅ Planned (awaiting approval)

---

## User Story

**As a** player
**I want to** experience a rich, engaging castle adventure story
**So that** I am entertained and want to replay to discover all paths

---

## Acceptance Criteria

- [ ] When I play, I encounter 28 total scenes with complete descriptions
- [ ] When I read scene descriptions, they are atmospheric and engaging (3-5 sentences)
- [ ] When I interact with NPCs, they have distinct personalities and dark humor
- [ ] When I reach endings, they feel earned and satisfying
- [ ] When I die, the death scenes are humorous and encourage retry
- [ ] When I make choices, the consequences are clear and interesting
- [ ] When I explore, I discover clever puzzles with fair solutions

---

## Definition of Done

- [ ] All 21 story scenes written with descriptions (5,500+ words total)
- [ ] All 6 death scenes written with dark humor
- [ ] All 5 endings written with full text from endings.md
- [ ] All 9 NPC dialogues implemented with personality quirks
- [ ] All 8 item descriptions written
- [ ] All 85+ choices implemented with clear text
- [ ] Story tone is consistently dark-humorous throughout
- [ ] Content reviewed for consistency and quality
- [ ] Tests validate all content is present (content completeness tests)
- [ ] Code committed with reference to this story

---

## Content Breakdown

### Scenes to Write: 28 Total

**Act I: Infiltration (8 scenes)**
- Scene 01: Outside Castle Walls (START)
- Scene 02: Climbing Garden Wall
- Scene 03: Courtyard - Hounds Released
- Scene 04: Sprint to Drawbridge
- Scene 05: Drawbridge Gate Drops
- Scene 06: Hide in Fountain (alternate)
- Scene 07: Castle Entrance Hall (HUB)
- Scene 08: Throne Room

**Act II: Exploration (10 scenes + variants)**
- Scene 09: Grand Hallway (HUB)
- Scene 10: Library
- Scene 11: Invisible Message Revealed
- Scene 12: Dungeon Entrance
- Scene 13: Troll's Lair + 13B: Troll Rewards
- Scene 14: Dragon's Cave + 14B & 14C: Dragon outcomes
- Scene 15: Kitchen (optional)
- Scene 16: Wizard's Study
- Scene 17: Armory (optional)
- Scene 18: Chapel (optional)

**Act III: Resolution (3 scenes + 5 endings)**
- Scene 19: Tower Staircase (HUB)
- Scene 20: Tower Landing
- Scene 21: Princess Chamber
- E1-E5: Five distinct endings

**Death Scenes (6 total)**
- D1: Front Gate Arrows
- D2: Hound Attack
- D3: Moat Spikes
- D4: Dragon Panic
- D5: Animated Armor
- D7: Wrong Riddle (troll pit trap)

---

## Writing Standards

**Scene Description Template:**
```
Scene: [TITLE]

[Opening sentence: Set atmosphere/location]
[Development: Describe key elements, sensory details]
[Situation: What's happening now, immediate choices]

Choices:
A) [Action with clear consequence]
B) [Alternative action]
C) [Third option if relevant]
D) [Return/escape option if applicable]
```

**Dark Humor Tone Guidelines:**
- Death is frequent but described comically
- NPCs have unexpected quirks (anxious dragon, polite troll)
- Self-aware narrator comments on absurdity
- Medieval setting with absurd situations (no modern references)
- Punny without being groan-worthy

**Example Dark Humor:**
- ❌ "You died. Game over." (too plain)
- ✅ "The hounds appreciate your optimism if not your tactical thinking. The castle awards you 'Most Confident Corpse.'" (dark + humorous)

---

## NPC Personality Guide

**1. Grizelda the Troll (Riddlemaster)**
- **Personality:** Polite, apologetic when you fail, loves riddles, vegetarian
- **Voice:** Formal but warm: "Oh dear, wrong answer I'm afraid. Do mind the spikes."
- **Quirk:** Collects riddles like others collect stamps

**2. Pyrrhus the Dragon (Anxious)**
- **Personality:** Cowardly, anxious, afraid of mice, apologizes profusely
- **Voice:** Nervous stammering: "AHHH! A human! Wait... you're smaller than I remember. Are you dangerous?"
- **Quirk:** Has anxiety about being a dragon, wants to be feared but is terrified

**3. Mervin the Wizard (Myopic)**
- **Personality:** Brilliant but nearly blind, constantly mistakes you for things
- **Voice:** Confused but confident: "Ah, you've brought my pizza! What? You're here to rescue someone? That's a strange topping."
- **Quirk:** Thinks everyone is pizza delivery

**4. Princess Elara (Unimpressed)**
- **Personality:** Sarcastic, capable, was planning own escape
- **Voice:** Dry and skeptical: "Oh wonderful, a rescuer. I was only three days away from finishing my rope ladder."
- **Quirk:** Evaluates your competence critically

**5. Infernal Hounds (Relentless but Dim)**
- **Personality:** Supernaturally fast but not smart
- **Voice:** (Narrator describes): "One trips over its own tail. The others stop to laugh."
- **Quirk:** Easily distracted by their own clumsiness

---

## Item Descriptions (8 Total)

| Item | Description |
|------|-------------|
| Magic Spectacles | "Dusty spectacles that reveal what eyes cannot see. The troll assures you they're prescription-free." |
| Dragon's Flame | "A vial of condensed dragon fire. Handle with extreme care. Or moderate care. Any care, really." |
| Tower Key | "An ornate key hidden behind the throne. Covered in dust and bad decisions." |
| Royal Seal | "The official seal of the kingdom. The wizard gave it to you thinking you were pizza. You didn't correct him." |
| Golden Goblet | "A jewel-encrusted goblet. Worth a fortune or one troll's cooperation, whichever you value more." |
| Moldy Cheese | "Ancient cheese from the kitchen. It's moving. Those are mice. Perfect for dragon negotiations." |
| Ancient Tome | "A leather-bound book about the castle's curse. The previous owners did not read the fine print." |
| Rusty Sword | "A sword so rusty it might give you tetanus just from looking at it. The armor strongly advises leaving it alone." |

---

## Puzzle Descriptions

**Puzzle 1: Escape the Hounds**
- **Setup:** Chase sequence across courtyard to drawbridge
- **Solution:** Pull lever to drop gate, trap hounds outside
- **Fair Clue:** Lever is prominently described, consequences are clear
- **Dark Humor:** Hounds' frustration is comically exaggerated

**Puzzle 2: Troll's Riddle**
- **Setup:** Answer riddle to earn magic spectacles
- **Riddle:** "I have cities but no houses, forests but no trees, water but no fish. What am I?"
- **Answer:** "A map"
- **Fair Clue:** All elements point to representation vs reality
- **Alternate Solution:** Bribe with golden goblet (if found)

**Puzzle 3: Invisible Ink Message**
- **Setup:** Map in library has invisible writing
- **Solution:** Use magic spectacles to reveal message about tower key location
- **Fair Clue:** Spectacles' description mentions "reveal what eyes cannot see"

**Puzzle 4: Dragon's Flame**
- **Setup:** Get dragon's flame without waking dragon
- **Solution:** Sneak carefully OR use cheese/mice to befriend dragon
- **Fair Clue:** Dragon is described as sleeping (sneak is obvious), cheese/mice is creative solution

**Puzzle 5: Frozen Staircase**
- **Setup:** Tower stairs are encased in magical ice
- **Solution:** Use dragon's flame to melt ice
- **Fair Clue:** Item description mentions "condensed dragon fire"

---

## Content Implementation Tasks

**Phase 1: Critical Path Content (Priority 0)**
```
□ Write 15 critical path scene descriptions
□ Write major NPC dialogue (Troll, Dragon, Princess)
□ Write 3 primary endings (E1, E2, E3)
□ Write critical item descriptions (3 items)
□ Write 3 main death scenes
```
**Estimated:** 4-6 hours

**Phase 2: Alternate Path Content (Priority 1)**
```
□ Write 3 alternate scenes (fountain, wizard, etc.)
□ Write wizard and minor NPC dialogue
□ Write 2 bonus endings (E4, E5)
□ Write optional item descriptions (4 items)
□ Write 3 additional death scenes
```
**Estimated:** 2-3 hours

**Phase 3: Polish & Optional Content (Priority 2)**
```
□ Write optional scenes (kitchen, armory, chapel)
□ Polish all descriptions for consistency
□ Review tone and humor throughout
□ Test all content flows naturally
```
**Estimated:** 2 hours

**Total:** 8-11 hours of writing

---

## Testing Requirements

**Content Completeness Tests:**
```python
def test_all_scenes_have_descriptions():
    """Verify all 28 scenes have non-empty descriptions."""
    scenes = Scene.objects.all()
    assert scenes.count() == 28
    for scene in scenes:
        assert len(scene.description) > 50  # At least 50 characters

def test_all_npcs_have_dialogue():
    """Verify all major NPCs have personality text."""
    # Implementation validates NPC dialogue exists

def test_all_items_have_descriptions():
    """Verify all 8 items have descriptions."""
    items = Item.objects.all()
    assert items.count() == 8
    for item in items:
        assert len(item.description) > 20

def test_all_endings_have_full_text():
    """Verify all 5 endings have complete text."""
    endings = Ending.objects.all()
    assert endings.count() == 5
    for ending in endings:
        assert len(ending.description) > 150  # Endings should be substantial
```

**Content Quality Manual Review:**
- Read through complete critical path for story coherence
- Verify dark humor tone is consistent
- Check for typos and grammatical errors
- Ensure no modern anachronisms
- Validate NPC personality consistency

---

## Related Stories

- Depends on: S-002 (Scene navigation structure)
- Related: S-003 (Item descriptions)
- Related: S-005 (Ending text)
- Blocks: S-007 (Frontend needs content to display)

---

**Document Status:** Ready for Development
**Created:** 2025-10-02
