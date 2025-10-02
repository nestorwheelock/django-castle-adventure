# S-001: Portable Django App Module

**Story Type**: User Story
**Priority**: High
**Estimate**: 1 day
**Sprint**: Sprint 1
**Status**: ✅ Planned (awaiting approval)

---

## User Story

**As a** Django developer
**I want to** install django-castle-adventure as a reusable app module
**So that** I can add the game to any Django project easily

---

## Acceptance Criteria

- [ ] When I install the package, I can add 'castle_adventure' to INSTALLED_APPS
- [ ] When I include the URLs, the game is accessible at /castle-adventure/
- [ ] When I run migrations, all models are created correctly
- [ ] When I deploy, the static files (CSS, ASCII art) are collected properly
- [ ] When I read the README, I understand how to integrate the module

---

## Definition of Done

- [ ] Package structure follows Django app conventions (models.py, views.py, urls.py, templates/)
- [ ] setup.py or pyproject.toml configured for pip installation
- [ ] Requirements.txt lists all dependencies
- [ ] Migration files created and tested (17 total tests minimum - following sudoku/tictactoe pattern)
- [ ] Static files properly configured
- [ ] README.md includes installation instructions
- [ ] Tests written and passing (>95% coverage)
- [ ] Code committed with reference to this story

---

## Technical Notes

**Package Structure:**
```
django-castle-adventure/
├── castle_adventure/        # Main Django app
│   ├── __init__.py
│   ├── models.py           # Scene, Choice, Item, GameState, Ending
│   ├── views.py            # Game views
│   ├── urls.py             # URL routing
│   ├── admin.py            # Django admin
│   ├── apps.py             # App config
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   └── castle_adventure/
│   ├── static/            # CSS, ASCII art files
│   │   └── castle_adventure/
│   └── tests/             # Test suite
├── setup.py               # Package configuration
├── requirements.txt       # Dependencies
├── README.md             # Documentation
└── LICENSE
```

**Dependencies:**
- Django >= 4.2
- Python >= 3.10

---

## Related Stories

- Blocked by: None (first story)
- Blocks: S-002, S-003, S-004, S-005, S-006, S-007 (all others depend on this)

---

**Document Status:** Ready for Development
**Created:** 2025-10-02
