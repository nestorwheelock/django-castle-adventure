# T-008: ASCII Art Creation

**Related Story:** S-006 (Story Content Implementation)
**Priority:** P2 Optional (can ship without)
**Estimate:** 3 hours
**Sprint:** Sprint 3
**Status:** Pending

---

## AI Coding Brief

**Role:** ASCII Artist + Content Creator
**Objective:** Create ASCII art illustrations for major scenes to enhance atmosphere

**User Request:** "Create ASCII art for the 15 key scenes listed in content-inventory.md"

---

## Constraints

### Allowed File Paths
- `castle_adventure/static/castle_adventure/ascii_art/` (new directory)
- `castle_adventure/static/castle_adventure/ascii_art/*.txt` (15 files)
- Update `scenes.json` fixture with ascii_art paths

### Forbidden Paths
- No template changes (that's T-009)

---

## Deliverables

### ASCII Art Files (15 total)

**From content-inventory.md:**
1. `01-castle-exterior.txt` (15 lines)
2. `02-garden-wall.txt` (12 lines)
3. `03-courtyard-hounds.txt` (18 lines)
4. `04-drawbridge.txt` (14 lines)
5. `05-entrance-hall.txt` (16 lines)
6. `06-throne-room.txt` (20 lines)
7. `07-grand-hallway.txt` (12 lines)
8. `08-library.txt` (15 lines)
9. `09-dungeon-troll.txt` (18 lines)
10. `10-dragon-cave.txt` (20 lines)
11. `11-wizard-study.txt` (16 lines)
12. `12-chapel.txt` (14 lines)
13. `13-tower-staircase.txt` (17 lines)
14. `14-princess-chamber.txt` (18 lines)
15. `15-castle-collapse.txt` (16 lines)

**Example ASCII Art:**
```
    /\
   /  \
  /    \
 /______\
|  GATE |
|  LOCK |
└──────┘
```

---

## Quality Standards

- **Max width:** 70 characters (fits in most terminals)
- **Style:** Medieval fantasy theme
- **Detail level:** Evocative, not realistic
- **Consistency:** Similar style across all art
- **Readability:** Clear at small sizes

---

## Definition of Done

- [ ] All 15 ASCII art pieces created
- [ ] Each piece saved as .txt file
- [ ] Scenes fixture updated with ascii_art file paths
- [ ] Art renders correctly in monospace font
- [ ] No broken characters or encoding issues
- [ ] At least 3 validation tests (art files exist, valid encoding, max width)
- [ ] Code committed with "feat(ascii-art): add atmospheric ASCII illustrations for key scenes"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 3 tests:**
1. All 15 ASCII art files exist
2. All files use valid UTF-8 encoding
3. No line exceeds 70 characters

---

## Dependencies

- **Blocks:** None (optional enhancement)
- **Depends on:** T-007 (scenes must exist to add art to)

---

**Created:** 2025-10-02
**Status:** Ready for Development
