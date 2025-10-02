"""
Tests for save and load game state system (T-005).
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from castle_adventure.models import Scene, Choice, Item, GameState
import json
from datetime import datetime


class AutoSaveTestCase(TestCase):
    """Tests for auto-save functionality."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Entrance',
            description='Dark entrance',
            scene_type='story'
        )
        self.scene2 = Scene.objects.create(
            scene_id='02',
            title='Hall',
            description='Grand hall',
            scene_type='story'
        )

        self.choice1 = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Enter hall',
            choice_letter='A'
        )

        self.key = Item.objects.create(
            item_id='key',
            name='Rusty Key',
            description='Opens doors',
            found_in_scene=self.scene1
        )

    def test_autosave_on_choice(self):
        """Test that making a choice auto-saves game state."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )
        original_updated = game_state.last_updated

        self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))

        game_state.refresh_from_db()
        self.assertGreater(game_state.last_updated, original_updated)
        self.assertEqual(game_state.current_scene, self.scene2)

    def test_autosave_on_item_pickup(self):
        """Test that picking up item auto-saves game state."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )
        original_updated = game_state.last_updated

        self.client.post(reverse('castle_adventure:pickup_item', args=['key']))

        game_state.refresh_from_db()
        self.assertGreater(game_state.last_updated, original_updated)
        self.assertIn('key', game_state.inventory)

    def test_autosave_updates_last_updated_timestamp(self):
        """Test that auto-save updates last_updated field."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))

        game_state.refresh_from_db()
        time_diff = (datetime.now(game_state.last_updated.tzinfo) - game_state.last_updated).total_seconds()
        self.assertLess(time_diff, 5)


class ManualSaveTestCase(TestCase):
    """Tests for manual save functionality."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )

    def test_manual_save_success(self):
        """Test manual save returns success."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.post(reverse('castle_adventure:save'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('castle_adventure:scene', args=[self.scene1.scene_id]))

    def test_manual_save_no_active_game(self):
        """Test manual save redirects to landing when no active game."""
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse('castle_adventure:save'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('castle_adventure:landing'))


class LoadGameTestCase(TestCase):
    """Tests for load game functionality."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )
        self.scene2 = Scene.objects.create(
            scene_id='02',
            title='Hall',
            description='Hall scene',
            scene_type='story'
        )

    def test_load_existing_game(self):
        """Test loading existing game redirects to current scene."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene2
        )

        response = self.client.get(reverse('castle_adventure:load'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/scene/02/', response.url)

    def test_load_game_no_save_found(self):
        """Test loading when no save exists returns error."""
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(reverse('castle_adventure:load'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/start/', response.url)

    def test_load_restores_correct_scene(self):
        """Test load restores player to correct scene."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene2
        )

        response = self.client.get(reverse('castle_adventure:load'))

        game_state.refresh_from_db()
        self.assertEqual(game_state.current_scene, self.scene2)


class NewGameTestCase(TestCase):
    """Tests for new game functionality."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )

    def test_new_game_creates_fresh_state(self):
        """Test new game creates fresh game state."""
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse('castle_adventure:new_game'), {'confirm_overwrite': 'true'}, follow=True)
        self.assertEqual(response.status_code, 200)

        game_state = GameState.objects.get(user=self.user)
        self.assertEqual(game_state.current_scene, self.scene1)
        self.assertEqual(game_state.choices_made, 0)
        self.assertEqual(len(game_state.inventory), 0)

    def test_new_game_requires_confirmation_with_existing_save(self):
        """Test new game requires confirmation when save exists."""
        self.client.login(username='testuser', password='testpass')

        existing_save = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            choices_made=5,
            items_collected=3
        )

        response = self.client.post(reverse('castle_adventure:new_game'))
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertTrue(data['requires_confirmation'])
        self.assertIn('existing_save', data)
        self.assertEqual(data['existing_save']['items'], 3)

    def test_new_game_deletes_old_save(self):
        """Test new game deletes old save when confirmed."""
        self.client.login(username='testuser', password='testpass')

        old_save = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            choices_made=10
        )
        old_save_id = old_save.id

        response = self.client.post(reverse('castle_adventure:new_game'), {'confirm_overwrite': 'true'})

        self.assertFalse(GameState.objects.filter(id=old_save_id).exists())


class SessionVsUserSavesTestCase(TestCase):
    """Tests for session-based vs user-based saves."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )

    def test_anonymous_user_creates_session_based_save(self):
        """Test anonymous users get session-based saves."""
        self.client.get(reverse('castle_adventure:start'))

        game_state = GameState.objects.first()
        self.assertIsNone(game_state.user)
        self.assertIsNotNone(game_state.session_key)

    def test_authenticated_user_creates_user_based_save(self):
        """Test authenticated users get user-based saves."""
        self.client.login(username='testuser', password='testpass')

        self.client.get(reverse('castle_adventure:start'))

        game_state = GameState.objects.get(user=self.user)
        self.assertEqual(game_state.user, self.user)
        self.assertIsNone(game_state.session_key)


class SaveLoadIntegrationTestCase(TestCase):
    """Integration tests for save/load system."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Entrance',
            description='Dark entrance',
            scene_type='story'
        )
        self.scene2 = Scene.objects.create(
            scene_id='02',
            title='Hall',
            description='Grand hall',
            scene_type='story'
        )

        self.choice1 = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Enter hall',
            choice_letter='A'
        )

        self.key = Item.objects.create(
            item_id='key',
            name='Rusty Key',
            description='Opens doors',
            found_in_scene=self.scene1
        )

    def test_save_logout_login_load_state_preserved(self):
        """Test state is preserved across logout/login."""
        self.client.login(username='testuser', password='testpass')

        self.client.get(reverse('castle_adventure:start'))
        game_state = GameState.objects.get(user=self.user)

        self.client.post(reverse('castle_adventure:pickup_item', args=['key']))
        self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))

        game_state_id = game_state.id
        self.client.logout()

        self.client.login(username='testuser', password='testpass')
        self.client.get(reverse('castle_adventure:load'))

        restored_state = GameState.objects.get(id=game_state_id)
        self.assertEqual(restored_state.current_scene, self.scene2)

    def test_complete_save_load_flow(self):
        """Test complete flow: start → progress → save → load."""
        self.client.login(username='testuser', password='testpass')

        self.client.get(reverse('castle_adventure:start'))
        self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))

        save_response = self.client.post(reverse('castle_adventure:save'))
        self.assertEqual(save_response.status_code, 302)

        load_response = self.client.get(reverse('castle_adventure:load'))
        self.assertEqual(load_response.status_code, 302)

        game_state = GameState.objects.get(user=self.user)
        self.assertEqual(game_state.current_scene, self.scene2)
