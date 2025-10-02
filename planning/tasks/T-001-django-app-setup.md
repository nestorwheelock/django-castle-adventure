# T-001: Django App Module Setup

**Related Story:** S-001 (Portable Django Module)
**Priority:** P0 Critical
**Estimate:** 2 hours
**Sprint:** Sprint 1
**Status:** Pending

---

## AI Coding Brief

**Role:** Backend Django Developer
**Objective:** Create the basic Django app structure for castle_adventure as a portable, reusable module

**User Request:** "Set up the Django app directory structure with all necessary files for a portable Django module"

---

## Constraints

### Allowed File Paths
- `castle_adventure/` (create new Django app)
- `castle_adventure/__init__.py`
- `castle_adventure/apps.py`
- `castle_adventure/models.py`
- `castle_adventure/views.py`
- `castle_adventure/urls.py`
- `castle_adventure/admin.py`
- `castle_adventure/migrations/`
- `castle_adventure/templates/castle_adventure/`
- `castle_adventure/static/castle_adventure/`
- `castle_adventure/tests/`
- `setup.py`
- `requirements.txt`
- `pyproject.toml`

### Forbidden Paths
- No modification to existing Django project settings
- No database operations yet (migrations come in T-002)

---

## Deliverables

### 1. Django App Structure
```
castle_adventure/
├── __init__.py
├── apps.py              # CastleAdventureConfig
├── models.py            # Empty for now
├── views.py             # Empty for now
├── urls.py              # URL routing stub
├── admin.py             # Admin registration stub
├── migrations/
│   └── __init__.py
├── templates/
│   └── castle_adventure/
│       └── .gitkeep
├── static/
│   └── castle_adventure/
│       ├── css/
│       ├── js/
│       └── ascii_art/
└── tests/
    ├── __init__.py
    ├── test_models.py
    ├── test_views.py
    └── test_integration.py
```

### 2. Package Configuration
- `setup.py` with package metadata
- `requirements.txt` with Django dependency
- `pyproject.toml` (optional, modern Python packaging)

### 3. Apps Configuration
```python
# apps.py
from django.apps import AppConfig

class CastleAdventureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'castle_adventure'
    verbose_name = 'Castle of Shadows Adventure Game'
```

---

## Definition of Done

- [ ] Django app directory created with standard structure
- [ ] All required files present (apps.py, urls.py, admin.py, etc.)
- [ ] setup.py configured for pip installation
- [ ] requirements.txt lists Django 4.2+
- [ ] Tests directory created with initial test files
- [ ] Static and templates directories created
- [ ] App can be imported: `from castle_adventure import apps`
- [ ] At least 5 tests written and passing (basic structure tests)
- [ ] Code committed with "feat(setup): create Django app module structure"
- [ ] GitHub issue closed with commit reference

---

## Test Requirements

**Minimum 5 tests:**
1. Test app config loads correctly
2. Test app name is 'castle_adventure'
3. Test templates directory exists
4. Test static directory exists
5. Test migrations directory exists

---

## Dependencies

- **Blocks:** T-002 (models need app structure)
- **Depends on:** None (first task)

---

**Created:** 2025-10-02
**Status:** Ready for Development
