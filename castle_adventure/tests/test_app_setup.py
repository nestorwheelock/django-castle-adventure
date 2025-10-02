"""
Tests for Django app module setup (T-001).
Following TDD: These tests are written BEFORE implementation.
"""
import os
from django.test import TestCase
from django.apps import apps
from castle_adventure.apps import CastleAdventureConfig


class AppSetupTestCase(TestCase):
    """Test basic app structure and configuration."""

    def test_app_config_loads_correctly(self):
        """Test that app config can be loaded."""
        app_config = apps.get_app_config('castle_adventure')
        self.assertIsNotNone(app_config)
        self.assertIsInstance(app_config, CastleAdventureConfig)

    def test_app_name_is_castle_adventure(self):
        """Test that app name is correctly set."""
        app_config = apps.get_app_config('castle_adventure')
        self.assertEqual(app_config.name, 'castle_adventure')

    def test_app_verbose_name_is_set(self):
        """Test that verbose name is set for admin."""
        app_config = apps.get_app_config('castle_adventure')
        self.assertEqual(app_config.verbose_name, 'Castle of Shadows Adventure Game')

    def test_templates_directory_exists(self):
        """Test that templates directory exists."""
        app_config = apps.get_app_config('castle_adventure')
        app_path = app_config.path
        templates_path = os.path.join(app_path, 'templates', 'castle_adventure')
        self.assertTrue(os.path.exists(templates_path),
                       f"Templates directory should exist at {templates_path}")

    def test_static_directory_exists(self):
        """Test that static directory exists."""
        app_config = apps.get_app_config('castle_adventure')
        app_path = app_config.path
        static_path = os.path.join(app_path, 'static', 'castle_adventure')
        self.assertTrue(os.path.exists(static_path),
                       f"Static directory should exist at {static_path}")

    def test_migrations_directory_exists(self):
        """Test that migrations directory exists."""
        app_config = apps.get_app_config('castle_adventure')
        app_path = app_config.path
        migrations_path = os.path.join(app_path, 'migrations')
        self.assertTrue(os.path.exists(migrations_path),
                       f"Migrations directory should exist at {migrations_path}")

    def test_tests_directory_exists(self):
        """Test that tests directory exists."""
        app_config = apps.get_app_config('castle_adventure')
        app_path = app_config.path
        tests_path = os.path.join(app_path, 'tests')
        self.assertTrue(os.path.exists(tests_path),
                       f"Tests directory should exist at {tests_path}")
