"""
Tests for inventory system (T-004).
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from castle_adventure.models import Scene, Choice, Item, GameState
import json


class PickupItemViewTestCase(TestCase):
    """Tests for pickup_item view."""

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

        self.key = Item.objects.create(
            item_id='key',
            name='Rusty Key',
            description='Opens doors',
            found_in_scene=self.scene1,
            icon='🔑'
        )

    def test_pickup_item_valid(self):
        """Test picking up an item in the current scene."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.post(reverse('castle_adventure:pickup_item', args=['key']))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('castle_adventure:scene', args=[self.scene1.scene_id]))

        game_state.refresh_from_db()
        self.assertIn('key', game_state.inventory)
        self.assertEqual(game_state.items_collected, 1)

    def test_pickup_item_duplicate_prevention(self):
        """Test that picking up same item twice doesn't duplicate."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        self.client.post(reverse('castle_adventure:pickup_item', args=['key']))
        response = self.client.post(reverse('castle_adventure:pickup_item', args=['key']))

        self.assertEqual(response.status_code, 302)
        game_state.refresh_from_db()

        self.assertEqual(game_state.inventory.count('key'), 1)
        self.assertEqual(game_state.items_collected, 1)

    def test_pickup_item_wrong_scene(self):
        """Test cannot pick up item from different scene."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene2
        )

        response = self.client.post(reverse('castle_adventure:pickup_item', args=['key']))
        self.assertEqual(response.status_code, 400)

        game_state.refresh_from_db()
        self.assertNotIn('key', game_state.inventory)


class ViewInventoryTestCase(TestCase):
    """Tests for view_inventory view."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Entrance',
            description='Dark entrance',
            scene_type='story'
        )

        self.key = Item.objects.create(
            item_id='key',
            name='Rusty Key',
            description='Opens doors',
            found_in_scene=self.scene1
        )
        self.sword = Item.objects.create(
            item_id='sword',
            name='Iron Sword',
            description='A trusty weapon',
            found_in_scene=self.scene1
        )

    def test_view_empty_inventory(self):
        """Test viewing inventory with no items."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.get(reverse('castle_adventure:inventory'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['items']), 0)

    def test_view_inventory_with_items(self):
        """Test viewing inventory with collected items."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )
        game_state.add_item('key')
        game_state.add_item('sword')

        response = self.client.get(reverse('castle_adventure:inventory'))
        self.assertEqual(response.status_code, 200)

        items = list(response.context['items'])
        item_ids = [item.item_id for item in items]

        self.assertIn('key', item_ids)
        self.assertIn('sword', item_ids)
        self.assertEqual(len(items), 2)


class GameStateInventoryMethodsTestCase(TestCase):
    """Tests for GameState inventory methods."""

    def setUp(self):
        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_add_item_to_inventory(self):
        """Test add_item adds to inventory list."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        game_state.add_item('key')
        game_state.refresh_from_db()

        self.assertIn('key', game_state.inventory)

    def test_add_item_increments_counter(self):
        """Test add_item increments items_collected."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        game_state.add_item('key')
        game_state.add_item('sword')
        game_state.refresh_from_db()

        self.assertEqual(game_state.items_collected, 2)

    def test_add_item_prevents_duplicates(self):
        """Test add_item doesn't add duplicate items."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        game_state.add_item('key')
        game_state.add_item('key')
        game_state.refresh_from_db()

        self.assertEqual(game_state.inventory.count('key'), 1)
        self.assertEqual(game_state.items_collected, 1)

    def test_has_item_returns_true(self):
        """Test has_item returns True for items in inventory."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )
        game_state.add_item('key')

        self.assertTrue(game_state.has_item('key'))

    def test_has_item_returns_false(self):
        """Test has_item returns False for items not in inventory."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        self.assertFalse(game_state.has_item('key'))


class InventoryIntegrationTestCase(TestCase):
    """Integration tests for inventory and choice requirements."""

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
            title='Locked Room',
            description='A locked door',
            scene_type='story'
        )

        self.key = Item.objects.create(
            item_id='key',
            name='Rusty Key',
            description='Opens doors',
            found_in_scene=self.scene1
        )

        self.locked_choice = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Unlock door',
            choice_letter='A',
            requires_item=self.key
        )

    def test_pickup_item_then_use_in_choice(self):
        """Test picking up item and using it to unlock choice."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        self.client.post(reverse('castle_adventure:pickup_item', args=['key']))

        response = self.client.post(
            reverse('castle_adventure:choice', args=[self.locked_choice.id])
        )
        self.assertEqual(response.status_code, 302)

        game_state.refresh_from_db()
        self.assertEqual(game_state.current_scene, self.scene2)

    def test_choice_blocked_without_required_item(self):
        """Test choice is blocked without required item."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.post(
            reverse('castle_adventure:choice', args=[self.locked_choice.id])
        )
        self.assertEqual(response.status_code, 400)

        game_state.refresh_from_db()
        self.assertEqual(game_state.current_scene, self.scene1)
