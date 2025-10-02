# S-007: Frontend Game Interface

**Story Type**: User Story
**Priority**: High
**Estimate**: 2 days
**Sprint**: Sprint 3
**Status**: ✅ Planned (awaiting approval)

---

## User Story

**As a** player
**I want to** interact with the game through an intuitive, atmospheric interface
**So that** I can focus on the story and feel immersed in the castle adventure

---

## Acceptance Criteria

- [ ] When I visit the game, I see an atmospheric dark-themed interface
- [ ] When I start a game, I see the opening scene with ASCII art
- [ ] When I read scenes, the text is readable and atmospheric
- [ ] When I view choices, they are clearly labeled (A, B, C, D)
- [ ] When I see my inventory, items are displayed with descriptions
- [ ] When I see ASCII art, it renders correctly in monospace font
- [ ] When I save/load, I get visual feedback that it worked
- [ ] When I use mobile, the interface is responsive and usable

---

## Definition of Done

- [ ] Base HTML template created with dark theme styling (13 tests)
- [ ] Game board view template displays scene, choices, ASCII art
- [ ] Inventory display component implemented
- [ ] Save/load UI components implemented
- [ ] Ending display template with achievements
- [ ] ASCII art renders correctly (monospace font, proper spacing)
- [ ] Responsive CSS for mobile/tablet/desktop
- [ ] Accessibility: keyboard navigation, screen reader support
- [ ] Tests written and passing (>95% coverage)
- [ ] Code committed with reference to this story

---

## UI Components

### 1. Main Game Screen Layout

```
╔══════════════════════════════════════════════════════════════╗
║                  CASTLE OF SHADOWS                           ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ┌────────────────────────────────────────────────────────┐ ║
║  │          ASCII ART OF CURRENT SCENE                    │ ║
║  │                                                        │ ║
║  │              🏰                                        │ ║
║  │          [Castle art here]                            │ ║
║  │                                                        │ ║
║  └────────────────────────────────────────────────────────┘ ║
║                                                              ║
║  OUTSIDE CASTLE WALLS                                        ║
║  ────────────────────────────────────────────────────────   ║
║                                                              ║
║  Dark, stormy night. Castle Shadowmere looms ominously      ║
║  before you. Thunder crashes. You hear screams from the     ║
║  tower. The princess needs rescue. Or does she?             ║
║                                                              ║
║  ────────────────────────────────────────────────────────   ║
║  WHAT DO YOU DO?                                            ║
║                                                              ║
║  [A] Climb the garden wall (stealthy)                       ║
║  [B] Knock on the front gate (bold)                         ║
║  [C] Turn back (cowardly)                                   ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║  Inventory: [Empty]                           [Save] [Menu] ║
╚══════════════════════════════════════════════════════════════╝
```

### 2. Inventory Panel (Expandable)

```
╔══════════════════════════════════════════════════════════════╗
║              YOUR INVENTORY (3 ITEMS)                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🔮 MAGIC SPECTACLES                                         ║
║     Dusty spectacles that reveal what eyes cannot see.      ║
║     The troll assures you they're prescription-free.         ║
║                                                              ║
║  🔥 DRAGON'S FLAME                                           ║
║     A vial of condensed dragon fire. Handle with extreme    ║
║     care. Or moderate care. Any care, really.               ║
║                                                              ║
║  🗝️ TOWER KEY                                                ║
║     An ornate key hidden behind the throne. Covered in      ║
║     dust and bad decisions.                                 ║
║                                                              ║
║  [Close Inventory]                                          ║
╚══════════════════════════════════════════════════════════════╝
```

### 3. Death Screen

```
╔══════════════════════════════════════════════════════════════╗
║                    💀 YOU DIED 💀                            ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  The hounds appreciate your optimism if not your tactical   ║
║  thinking. At least your death was quick.                   ║
║                                                              ║
║  The castle awards you the achievement:                     ║
║  "MOST CONFIDENT CORPSE"                                    ║
║                                                              ║
║  Deaths: 3                                                  ║
║  Choices Made: 7                                            ║
║                                                              ║
║  [Try Again]  [Main Menu]                                   ║
╚══════════════════════════════════════════════════════════════╝
```

### 4. Ending Screen

```
╔══════════════════════════════════════════════════════════════╗
║                  ⭐ HEROIC RESCUE ⭐                          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Princess Elara carefully evaluates you. She notices the    ║
║  magic spectacles, the dragon's flame, the careful way you  ║
║  solved puzzles instead of breaking things.                 ║
║                                                              ║
║  "Not bad," she finally says. "You actually used your       ║
║  brain. I respect that."                                    ║
║                                                              ║
║  [... full ending text ...]                                 ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║        ACHIEVEMENT UNLOCKED: HEROIC RESCUE                   ║
║        The classic ending. Well done!                        ║
╠══════════════════════════════════════════════════════════════╣
║  Endings Discovered: 1 / 5                                  ║
║                                                              ║
║  [Play Again]  [View All Endings]  [Main Menu]              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Visual Design Specifications

**Color Scheme (Dark Medieval Theme):**
- Background: `#1a1a1a` (near black)
- Primary Text: `#e0e0e0` (light gray)
- Accent/Borders: `#8b0000` (dark red)
- Hover/Active: `#b22222` (firebrick)
- Inventory/Panel BG: `#2a2a2a` (dark gray)
- ASCII Art: `#00ff00` (classic green terminal)

**Typography:**
- Scene descriptions: `Georgia, serif` (readable, atmospheric)
- ASCII Art: `'Courier New', monospace` (fixed-width for ASCII)
- UI elements: `'Trebuchet MS', sans-serif` (clean, readable)
- Font sizes: 16px base, 18px for descriptions, 14px for UI

**Layout:**
- Max width: 900px (optimal reading)
- Centered on page
- Padding: 20px on mobile, 40px on desktop
- Box shadows for depth
- Subtle borders using ASCII characters (`╔═╗`)

---

## Responsive Design

**Desktop (> 1024px):**
- Full ASCII art display
- Side-by-side inventory panel (optional)
- Larger text (18px base)

**Tablet (768-1024px):**
- Slightly smaller ASCII art
- Stacked inventory panel
- 16px base text

**Mobile (< 768px):**
- Simplified ASCII art (smaller or text-only)
- Vertical layout
- Larger touch targets for choices (48px min)
- Collapsible inventory
- 14px base text

---

## Accessibility Requirements

**Keyboard Navigation:**
- Tab through choices (A, B, C, D)
- Enter/Space to select choice
- Esc to open menu
- I for inventory

**Screen Reader Support:**
- ARIA labels for all interactive elements
- Alt text for ASCII art (describe scene)
- Skip to main content link
- Focus indicators visible

**Visual Accessibility:**
- High contrast mode option
- Text size adjustment (100%, 125%, 150%)
- Focus outlines clearly visible
- No color-only information

---

## Templates to Create

**1. base.html**
- Page structure
- CSS/JS includes
- Navigation header
- Footer

**2. game_board.html**
- Current scene display
- ASCII art rendering
- Choice buttons
- Inventory sidebar

**3. start_game.html**
- New game / Continue game buttons
- Saved game info (if exists)
- Game intro/lore

**4. ending.html**
- Ending text display
- Achievement unlock
- Replay options
- Endings collection link

**5. inventory.html** (component/modal)
- Item list with descriptions
- Dismissable overlay

**6. endings_collection.html**
- Grid of all endings
- Locked/unlocked status
- Progress tracker

---

## CSS Architecture

**File Structure:**
```
static/castle_adventure/css/
├── base.css           # Reset, typography, layout
├── theme.css          # Colors, dark theme
├── components.css     # Reusable UI components
├── game.css           # Game-specific styling
└── responsive.css     # Media queries
```

**Key Classes:**
```css
.game-container       /* Main wrapper */
.scene-display        /* Scene description area */
.ascii-art           /* Monospace ASCII rendering */
.choice-list         /* Choice buttons container */
.choice-btn          /* Individual choice button */
.inventory-panel     /* Inventory sidebar */
.item-card           /* Individual item display */
.ending-screen       /* Ending display */
.achievement-badge   /* Achievement unlock notification */
```

---

## JavaScript Functionality (Minimal)

**Required JS:**
- Auto-save indicator (show "Saving..." briefly after choice)
- Inventory toggle (show/hide panel)
- Keyboard shortcuts
- Choice confirmation (optional, for destructive choices)
- Ending unlock animation

**No Heavy JS:**
- Game logic stays server-side (Django views)
- Page reloads for scene transitions (or HTMX for smoother UX)
- Progressive enhancement (works without JS)

---

## ASCII Art Rendering

**Technical Requirements:**
```css
.ascii-art {
    font-family: 'Courier New', 'Courier', monospace;
    font-size: 14px;
    line-height: 1.2;
    white-space: pre;  /* Preserve spacing */
    color: #00ff00;    /* Classic terminal green */
    background: #0a0a0a;
    padding: 20px;
    border: 2px solid #8b0000;
    overflow-x: auto;  /* Horizontal scroll if needed */
}
```

**Mobile Optimization:**
- Reduce font size on mobile (10-12px)
- Allow horizontal scroll
- Optional: Text-only mode for very small screens

---

## Performance Considerations

**Optimization:**
- Minify CSS and JS
- Use Django template caching
- Lazy load non-critical assets
- Compress ASCII art (it's just text)
- Browser caching for static assets

**Page Load:**
- Target < 2 seconds
- Minimal external dependencies
- No large images (ASCII art only)

---

## Testing Requirements

**Visual Regression Tests:**
- Screenshot comparisons for key scenes
- ASCII art renders correctly
- Responsive layouts work on all sizes

**Functional Tests:**
- Choice buttons are clickable
- Inventory opens/closes
- Save indicator appears
- Keyboard navigation works
- Screen reader announces content

**Cross-Browser Testing:**
- Chrome, Firefox, Safari, Edge
- Mobile browsers (iOS Safari, Chrome Android)
- ASCII art renders consistently

---

## Related Stories

- Depends on: S-001 (Django module), S-002 (Scene data), S-006 (Story content)
- Related: S-003 (Inventory display), S-004 (Save UI), S-005 (Ending UI)

---

**Document Status:** Ready for Development
**Created:** 2025-10-02
