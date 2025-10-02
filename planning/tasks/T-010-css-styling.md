# T-010: CSS Styling and Theme

**Related Story:** S-007 (Frontend Game Interface)
**Priority:** P1 Important
**Estimate:** 3 hours
**Sprint:** Sprint 3
**Status:** Pending

---

## AI Coding Brief

**Role:** Frontend Developer / UI Designer
**Objective:** Create dark medieval-themed CSS for all game interfaces

**User Request:** "Implement CSS styling for dark-humorous 80s text adventure aesthetic with responsive design"

---

## Constraints

### Allowed File Paths
- `castle_adventure/static/castle_adventure/css/`
- `castle_adventure/static/castle_adventure/css/base.css`
- `castle_adventure/static/castle_adventure/css/theme.css`
- `castle_adventure/static/castle_adventure/css/components.css`
- `castle_adventure/static/castle_adventure/css/responsive.css`

### Forbidden Paths
- No JavaScript (keep it simple, progressive enhancement only)

---

## Deliverables

### 1. Base CSS (Reset & Typography)
```css
/* base.css */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Georgia, serif;
    font-size: 16px;
    line-height: 1.6;
    background: #1a1a1a;
    color: #e0e0e0;
}

.game-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px;
}

h1 { font-size: 32px; font-weight: bold; }
h2 { font-size: 24px; }
h3 { font-size: 20px; }
```

### 2. Theme CSS (Colors & Dark Medieval Style)
```css
/* theme.css */
:root {
    --bg-dark: #1a1a1a;
    --bg-medium: #2a2a2a;
    --text-light: #e0e0e0;
    --accent-red: #8b0000;
    --accent-red-hover: #b22222;
    --ascii-green: #00ff00;
}

.scene-display {
    background: var(--bg-medium);
    border: 2px solid var(--accent-red);
    padding: 20px;
    margin: 20px 0;
}

.ascii-art {
    font-family: 'Courier New', monospace;
    font-size: 14px;
    line-height: 1.2;
    color: var(--ascii-green);
    background: #0a0a0a;
    padding: 20px;
    border: 2px solid var(--accent-red);
    overflow-x: auto;
}
```

### 3. Components CSS (Buttons, Forms, Panels)
```css
/* components.css */
.btn {
    display: inline-block;
    padding: 12px 24px;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    border: 2px solid var(--accent-red);
    background: var(--bg-dark);
    color: var(--text-light);
    cursor: pointer;
    transition: all 0.3s;
}

.btn:hover {
    background: var(--accent-red-hover);
}

.choice-btn {
    width: 100%;
    text-align: left;
    margin: 10px 0;
    padding: 15px;
}

.choice-btn.locked {
    opacity: 0.5;
    cursor: not-allowed;
    background: #555;
}

.inventory-bar {
    background: var(--bg-medium);
    border: 1px solid var(--accent-red);
    padding: 15px;
}

.item-icon {
    font-size: 24px;
    margin-right: 10px;
}
```

### 4. Responsive CSS (Mobile, Tablet, Desktop)
```css
/* responsive.css */
@media (max-width: 768px) {
    .game-container {
        padding: 20px 10px;
    }

    .ascii-art {
        font-size: 10px;
    }

    .choice-btn {
        min-height: 60px; /* Larger touch targets */
    }

    h1 {
        font-size: 24px;
    }
}

@media (min-width: 1024px) {
    .ascii-art {
        font-size: 16px;
    }
}
```

---

## Design Specifications

**Color Palette:**
- Background: #1a1a1a (dark gray)
- Panel BG: #2a2a2a (lighter gray)
- Text: #e0e0e0 (light gray)
- Borders/Accent: #8b0000 (dark red)
- Hover: #b22222 (firebrick)
- ASCII Art: #00ff00 (terminal green)

**Typography:**
- Body: Georgia, serif (16px)
- ASCII Art: Courier New, monospace (14px)
- Buttons: Trebuchet MS, sans-serif (18px bold)

**Spacing:**
- Container padding: 40px desktop, 20px mobile
- Section margins: 20px
- Button padding: 12px 24px

---

## Definition of Done

- [ ] All 4 CSS files created
- [ ] Dark medieval theme implemented
- [ ] Responsive design (mobile, tablet, desktop)
- [ ] ASCII art renders correctly (monospace, green)
- [ ] Buttons have hover states
- [ ] High contrast (WCAG AA compliant)
- [ ] Touch-friendly buttons on mobile (48px minimum)
- [ ] No horizontal scroll on mobile
- [ ] At least 5 visual tests (CSS loads, colors correct, responsive)
- [ ] Code committed with "feat(css): implement dark medieval theme with responsive design"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 5 tests:**
1. All CSS files load without errors
2. Color variables defined correctly
3. Responsive breakpoints trigger
4. ASCII art is monospace
5. Buttons are accessible (contrast ratio >4.5:1)

---

## Dependencies

- **Blocks:** None (completes frontend)
- **Depends on:** T-009 (templates must exist to style)

---

**Created:** 2025-10-02
**Status:** Ready for Development
