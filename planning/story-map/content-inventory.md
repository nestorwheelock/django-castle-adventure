# Content Inventory

**Project:** django-castle-adventure v1.0.0
**Purpose:** Track all content assets for development

---

## Scenes Inventory

### Total Scenes: 28

**Story Scenes:** 21
**Death Scenes:** 6
**Ending Scenes:** 5
**Hub Scenes:** 3 (convergence points)

### Scene Status Tracker

| Scene ID | Scene Name | Type | Status | Priority | Est. Words |
|----------|------------|------|--------|----------|------------|
| 01 | Outside Castle Walls | Story | ✅ Planned | P0 Critical | 100 |
| 02 | Climbing Garden Wall | Story | ✅ Planned | P0 Critical | 80 |
| 03 | Courtyard - Hounds | Story | ✅ Planned | P0 Critical | 120 |
| 04 | Sprint to Drawbridge | Story | ✅ Planned | P0 Critical | 100 |
| 05 | Drawbridge Gate Drops | Story | ✅ Planned | P0 Critical | 80 |
| 06 | Hide in Fountain | Story | ✅ Planned | P1 Alternate | 90 |
| 07 | Castle Entrance Hall | Hub | ✅ Planned | P0 Critical | 110 |
| 08 | Throne Room | Story | ✅ Planned | P0 Critical | 130 |
| 09 | Grand Hallway | Hub | ✅ Planned | P0 Critical | 100 |
| 10 | Library | Story | ✅ Planned | P0 Critical | 120 |
| 11 | Invisible Message | Story | ✅ Planned | P0 Critical | 70 |
| 12 | Dungeon Entrance | Story | ✅ Planned | P0 Critical | 90 |
| 13 | Troll's Lair | Story | ✅ Planned | P0 Critical | 150 |
| 13B | Troll Rewards You | Story | ✅ Planned | P0 Critical | 90 |
| 14 | Dragon's Cave | Story | ✅ Planned | P0 Critical | 140 |
| 14B | Got Dragon's Flame | Story | ✅ Planned | P0 Critical | 70 |
| 14C | Mouse Negotiation | Story | ✅ Planned | P1 Alternate | 110 |
| 15 | Kitchen | Story | ✅ Planned | P2 Optional | 80 |
| 16 | Wizard's Study | Story | ✅ Planned | P1 Alternate | 130 |
| 17 | Armory | Story | ✅ Planned | P2 Optional | 100 |
| 18 | Chapel | Story | ✅ Planned | P2 Optional | 110 |
| 19 | Tower Staircase | Hub | ✅ Planned | P0 Critical | 100 |
| 20 | Tower Landing | Story | ✅ Planned | P0 Critical | 90 |
| 21 | Princess Chamber | Story | ✅ Planned | P0 Critical | 140 |
| 22 | Secret Passage | Story | ✅ Planned | P3 Bonus | 80 |
| 23 | Guard Room | Story | ✅ Planned | P2 Optional | 90 |

**Death Scenes:**
| Scene ID | Death Name | Trigger | Status | Est. Words |
|----------|------------|---------|--------|------------|
| D1 | Front Gate Arrows | Try front gate | ✅ Planned | 60 |
| D2 | Hound Attack | Fight hounds | ✅ Planned | 70 |
| D3 | Moat Spikes | Jump moat | ✅ Planned | 65 |
| D4 | Dragon Panic | Wake dragon | ✅ Planned | 80 |
| D5 | Animated Armor | Steal sword | ✅ Planned | 75 |
| D6 | Freeze in Fountain | Stay too long | ✅ Planned | 60 |
| D7 | Wrong Riddle | Troll riddle fail | ✅ Planned | 70 |
| D8 | Troll Strength | Attack troll | ✅ Planned | 65 |
| D9 | Dragon Crushing | Taunt with mice | ✅ Planned | 70 |

**Ending Scenes:**
| Scene ID | Ending Name | Type | Status | Est. Words |
|----------|-------------|------|--------|------------|
| E1 | Heroic Rescue | Victory | ✅ Planned | 200 |
| E2 | Tragic Betrayal | Dark Twist | ✅ Planned | 180 |
| E3 | Mutual Escape | Partnership | ✅ Planned | 220 |
| E4 | Castle Collapse | Comedy | ✅ Planned | 210 |
| E5 | New Ruler | Secret | ✅ Planned | 250 |

**Total Word Count Estimate:** ~5,500 words

---

## Items Inventory

### Total Items: 8

| Item ID | Item Name | Location Found | Required For | Type | Status |
|---------|-----------|----------------|--------------|------|--------|
| ITEM_001 | Magic Spectacles | Troll's Lair (Scene 13) | Read invisible ink | Critical | ✅ Planned |
| ITEM_002 | Dragon's Flame | Dragon's Cave (Scene 14) | Melt tower ice | Critical | ✅ Planned |
| ITEM_003 | Tower Key | Behind Throne (Scene 08) | Unlock princess door | Critical | ✅ Planned |
| ITEM_004 | Royal Seal | Wizard's Study (Scene 16) | Alternate commands | Optional | ✅ Planned |
| ITEM_005 | Golden Goblet | Throne Room (Scene 08) | Bribe troll | Optional | ✅ Planned |
| ITEM_006 | Moldy Cheese | Kitchen (Scene 15) | Attract mice (dragon) | Optional | ✅ Planned |
| ITEM_007 | Ancient Tome | Library (Scene 10) | Lore/hints | Optional | ✅ Planned |
| ITEM_008 | Rusty Sword | Armory (Scene 17) | Cursed (triggers death) | Trap | ✅ Planned |

**Critical Path Items:** 3 (Spectacles, Flame, Key)
**Optional Items:** 4 (Seal, Goblet, Cheese, Tome)
**Trap Items:** 1 (Sword)

---

## NPCs Inventory

### Total NPCs: 9

| NPC ID | NPC Name | Location | Role | Personality | Status |
|--------|----------|----------|------|-------------|--------|
| NPC_001 | Infernal Hounds | Courtyard (Scene 03) | Chase sequence | Relentless, dim | ✅ Planned |
| NPC_002 | Grizelda (Troll) | Dungeon (Scene 13) | Riddle challenge | Polite, loves riddles | ✅ Planned |
| NPC_003 | Pyrrhus (Dragon) | Dragon's Cave (Scene 14) | Item guardian | Anxious, afraid of mice | ✅ Planned |
| NPC_004 | Mervin (Wizard) | Wizard's Study (Scene 16) | Item giver | Myopic, confused | ✅ Planned |
| NPC_005 | Princess Elara | Tower Chamber (Scene 21) | Quest objective | Sarcastic, capable | ✅ Planned |
| NPC_006 | Ghostly Guards | Entrance Hall (Scene 07) | Atmospheric | Harmless, warning | ✅ Planned |
| NPC_007 | Castle Mice | Kitchen (Scene 15) | Puzzle item | Numerous, useful | ✅ Planned |
| NPC_008 | Animated Armor | Armory (Scene 17) | Guardian/trap | Dutiful, aggressive | ✅ Planned |
| NPC_009 | Talking Skull | Chapel (Scene 18) | Lore/hints | Helpful, punny | ✅ Planned |

**Major NPCs (dialogue, puzzles):** 5 (Troll, Dragon, Wizard, Princess, Hounds)
**Minor NPCs (atmospheric):** 4 (Guards, Mice, Armor, Skull)

---

## Puzzles Inventory

### Total Puzzles: 5

| Puzzle ID | Puzzle Name | Location | Solution | Type | Status |
|-----------|-------------|----------|----------|------|--------|
| PZ_001 | Escape the Hounds | Courtyard (Scene 03-05) | Drop drawbridge gate | Action | ✅ Planned |
| PZ_002 | Troll's Riddle | Dungeon (Scene 13) | Answer "a map" OR bribe | Logic | ✅ Planned |
| PZ_003 | Invisible Ink Message | Library (Scene 10-11) | Use magic spectacles | Item-based | ✅ Planned |
| PZ_004 | Get Dragon's Flame | Dragon's Cave (Scene 14) | Sneak OR use mice | Stealth/Negotiation | ✅ Planned |
| PZ_005 | Frozen Staircase | Tower (Scene 19) | Use dragon's flame | Item-based | ✅ Planned |

**Critical Path Puzzles:** 5 (all required to complete game)
**Optional Puzzles:** 0 (but alternate solutions exist)

---

## ASCII Art Inventory

### Total ASCII Art Pieces: 15

| Art ID | Subject | Scene(s) | Size (lines) | Status |
|--------|---------|----------|--------------|--------|
| ART_001 | Castle Exterior | Scene 01 | 15 | 📝 To Write |
| ART_002 | Garden Wall | Scene 02 | 12 | 📝 To Write |
| ART_003 | Courtyard + Hounds | Scene 03 | 18 | 📝 To Write |
| ART_004 | Drawbridge | Scene 04-05 | 14 | 📝 To Write |
| ART_005 | Entrance Hall | Scene 07 | 16 | 📝 To Write |
| ART_006 | Throne Room | Scene 08 | 20 | 📝 To Write |
| ART_007 | Grand Hallway | Scene 09 | 12 | 📝 To Write |
| ART_008 | Library | Scene 10 | 15 | 📝 To Write |
| ART_009 | Dungeon/Troll | Scene 13 | 18 | 📝 To Write |
| ART_010 | Dragon's Cave | Scene 14 | 20 | 📝 To Write |
| ART_011 | Wizard's Study | Scene 16 | 16 | 📝 To Write |
| ART_012 | Chapel | Scene 18 | 14 | 📝 To Write |
| ART_013 | Tower Staircase | Scene 19 | 17 | 📝 To Write |
| ART_014 | Princess Chamber | Scene 21 | 18 | 📝 To Write |
| ART_015 | Castle Collapse | Scene E4 | 16 | 📝 To Write |

**Total Lines of ASCII Art:** ~231 lines

---

## Choices Inventory

### Total Choices: ~85 choices across all scenes

**Choice Distribution:**
- Average 3 choices per story scene
- 1-2 choices for death scenes (try again/quit)
- 1-4 choices for ending scenes (epilogue options)

**Choice Types:**
| Type | Count | Examples |
|------|-------|----------|
| Navigation | 30 | "Go to library", "Return to hallway" |
| Action | 25 | "Pull lever", "Sneak past dragon" |
| Dialogue | 15 | "Ask about princess", "Play along with wizard" |
| Item Use | 10 | "Use spectacles", "Give cheese to mice" |
| Combat/Risk | 5 | "Fight hounds", "Attack troll" |

---

## Content Creation Tasks (for BUILD Phase)

### Phase 1: Core Content (Priority 0 - Critical Path)
- [ ] Write 15 critical path scene descriptions
- [ ] Write 3 primary death scene descriptions
- [ ] Write 2 primary endings (E1, E2)
- [ ] Create 8 critical ASCII art pieces
- [ ] Define all item descriptions
- [ ] Write major NPC dialogue

**Estimated Time:** 4-6 hours

### Phase 2: Alternate Content (Priority 1)
- [ ] Write 3 alternate path scenes
- [ ] Write 3 additional death scenes
- [ ] Write 1 additional ending (E3)
- [ ] Create 4 additional ASCII art pieces
- [ ] Write minor NPC dialogue

**Estimated Time:** 2-3 hours

### Phase 3: Optional Content (Priority 2-3)
- [ ] Write 3 optional scenes (kitchen, armory, chapel)
- [ ] Write 2 bonus endings (E4, E5)
- [ ] Create 3 bonus ASCII art pieces
- [ ] Polish all content

**Estimated Time:** 2-3 hours

**Total Content Creation Time:** 8-12 hours

---

## Content Quality Checklist

**For Each Scene:**
- [ ] 3-5 sentence description (atmospheric, concise)
- [ ] Clear choices with consequences
- [ ] Consistent dark humor tone
- [ ] No modern anachronisms
- [ ] Proper grammar and spelling
- [ ] Connected to story graph correctly

**For Each NPC:**
- [ ] Distinct personality quirk
- [ ] Consistent dialogue voice
- [ ] Serves story purpose
- [ ] Dark humor elements
- [ ] Clear interaction mechanics

**For Each Item:**
- [ ] Clear description
- [ ] Obvious or hinted use
- [ ] Fits medieval fantasy setting
- [ ] Integrated into puzzles

**For Each Ending:**
- [ ] Feels earned based on choices
- [ ] Distinct from other endings
- [ ] Dark humor maintained
- [ ] Satisfying conclusion
- [ ] 180-250 words

---

## Testing Content Checklist

**Story Graph Tests:**
- [ ] All scenes reachable from START
- [ ] No orphaned scenes
- [ ] All endings reachable
- [ ] Critical path playable (15 scenes)
- [ ] No infinite loops
- [ ] All item requirements satisfied

**Content Quality Tests:**
- [ ] All scene descriptions present
- [ ] All choices lead to valid scenes
- [ ] All NPCs have dialogue
- [ ] All items have descriptions
- [ ] ASCII art renders correctly
- [ ] Tone consistency maintained

**Playthrough Tests:**
- [ ] Critical path completable (START → E1)
- [ ] Alternate paths work (E2, E3)
- [ ] Secret ending achievable (E5)
- [ ] Death scenes trigger correctly
- [ ] Items unlock correct choices
- [ ] Save/load preserves story state

---

## Content Metadata

**Genre:** Dark-Humorous Text Adventure
**Rating:** PG-13 (comedic violence, dark themes, no gore/profanity)
**Target Audience:** Retro game fans, puzzle enthusiasts, CYOA lovers
**Playtime:** 10-15 minutes (single playthrough)
**Replayability:** High (5 endings, multiple paths)
**Difficulty:** Medium (puzzles are fair, deaths are frequent but humorous)

**Writing Style:**
- **Tone:** Darkly humorous, self-aware, absurd
- **POV:** Second person ("You enter the castle...")
- **Tense:** Present tense ("The dragon snores...")
- **Voice:** Slightly sardonic narrator

---

## Version History

**v1.0.0 (Current):**
- 28 scenes total
- 8 items
- 9 NPCs
- 5 puzzles
- 5 endings
- 15 ASCII art pieces

**Future Versions (Planned):**
- **v2.0.0:** +15 scenes (side quests), +3 items, +2 NPCs, +2 endings
- **v3.0.0:** RPG stats, combat system, +20 scenes
- **v4.0.0:** Multiplayer, +30 scenes, social features

---

**Document Status:** Complete - Content Inventory Ready
**Last Updated:** 2025-10-02
