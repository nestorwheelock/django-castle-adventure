"""
Tests for admin registration (T-002).
"""
from django.test import TestCase
from django.contrib import admin
from castle_adventure.models import Scene, Choice, Item, GameState, Ending, EndingUnlock


class AdminRegistrationTestCase(TestCase):
    """Test all models are registered in admin."""

    def test_all_models_registered_in_admin(self):
        """Test that all models are registered in Django admin."""
        self.assertIn(Scene, admin.site._registry)
        self.assertIn(Choice, admin.site._registry)
        self.assertIn(Item, admin.site._registry)
        self.assertIn(GameState, admin.site._registry)
        self.assertIn(Ending, admin.site._registry)
        self.assertIn(EndingUnlock, admin.site._registry)
