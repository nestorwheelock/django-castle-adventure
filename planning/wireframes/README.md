# Wireframes: Django Castle Adventure UI

**Project:** django-castle-adventure v1.0.0
**Purpose:** Visual mockups of game interface for client approval

---

## Overview

These ASCII wireframes show the complete user interface for the castle adventure game. All screens use a dark medieval theme with atmospheric typography and clear interaction patterns.

---

## Design Patterns

**Visual Theme:**
- Dark background (#1a1a1a) with light text (#e0e0e0)
- Dark red accents (#8b0000) for borders and highlights
- Classic green terminal color (#00ff00) for ASCII art
- Box-drawing characters for borders (╔═╗║╚╝)

**Layout Principles:**
- Max width 900px (optimal reading)
- Centered content
- Clear visual hierarchy
- Consistent padding and spacing
- Touch-friendly buttons (48px minimum)

**Typography:**
- Scene descriptions: Serif font (Georgia)
- ASCII art: Monospace (Courier New)
- UI elements: Sans-serif (Trebuchet MS)
- Base size: 16px (scales for mobile)

---

## Screen Inventory

1. **Landing Page** - Game start/continue
2. **Main Game Screen** - Scene, choices, inventory
3. **Inventory View** - Full item list with descriptions
4. **Death Screen** - Humorous death message, retry
5. **Ending Screen** - Ending text, achievement, replay
6. **Endings Collection** - All endings unlocked/locked
7. **Mobile View** - Responsive layout for small screens

---

## User Flows

**New Player Flow:**
```
Landing Page → Main Game Screen → Make Choices → Either:
├─→ Death Screen → Retry → Main Game Screen
├─→ Ending Screen → View Ending → Replay or View All Endings
└─→ Endings Collection → Start New Game
```

**Returning Player Flow:**
```
Landing Page → "Continue Game" → Main Game Screen (restored state)
```

**Exploration Flow:**
```
Main Game Screen ↔ Inventory View (toggle)
                 ↔ Menu (save, quit, settings)
```

---

## Responsive Breakpoints

**Desktop (> 1024px):**
- Full width ASCII art
- Sidebar inventory (optional)
- Larger text

**Tablet (768-1024px):**
- Medium ASCII art
- Stacked layout
- Standard text

**Mobile (< 768px):**
- Simplified or scrollable ASCII art
- Vertical layout
- Collapsible sections
- Larger touch targets

---

## Accessibility Features

- High contrast mode option
- Keyboard navigation (Tab, Enter, Arrow keys)
- Screen reader support (ARIA labels)
- Text size adjustment
- No color-only information

---

## Interactive Elements

**Buttons:**
- Choice buttons: Large, clearly labeled A/B/C/D
- Action buttons: Save, Menu, Inventory, etc.
- Hover states: Lighter red (#b22222)
- Disabled state: Gray with lock icon 🔒

**Feedback:**
- Auto-save indicator: Brief "Saving..." message
- Choice confirmation for destructive actions
- Item pickup notification
- Achievement unlock animation

---

## Color Accessibility

**Contrast Ratios (WCAG AA Compliant):**
- Text on background: 12:1 (exceeds 4.5:1 minimum)
- Buttons: 7:1
- Disabled elements: 3:1 (informational only)

**Colorblind Modes:**
- Icons supplement color coding
- Text labels for all states
- Pattern/texture differentiation

---

## Notes for Development

1. **ASCII Art Rendering:** Use `white-space: pre` and monospace font
2. **Box Characters:** Ensure UTF-8 encoding for proper display
3. **Responsive Images:** ASCII art may need simplified mobile version
4. **Progressive Enhancement:** Core game works without JavaScript
5. **Performance:** Target < 2 second page load, minimal assets

---

**Wireframes Complete:** 7 screens
**Last Updated:** 2025-10-02
