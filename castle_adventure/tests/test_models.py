"""
Tests for database models (T-002).
Following TDD: These tests are written BEFORE models are implemented.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from castle_adventure.models import Scene, Choice, Item, GameState, Ending, EndingUnlock


class SceneModelTestCase(TestCase):
    """Test Scene model."""

    def test_create_scene(self):
        """Test creating a basic scene."""
        scene = Scene.objects.create(
            scene_id='01',
            title='Outside Castle Walls',
            description='A dark and stormy night...',
            scene_type='story'
        )
        self.assertEqual(scene.scene_id, '01')
        self.assertEqual(scene.title, 'Outside Castle Walls')
        self.assertFalse(scene.is_ending)
        self.assertFalse(scene.is_death)

    def test_scene_id_unique(self):
        """Test that scene_id must be unique."""
        Scene.objects.create(scene_id='01', title='Scene 1', scene_type='story')
        with self.assertRaises(IntegrityError):
            Scene.objects.create(scene_id='01', title='Duplicate', scene_type='story')

    def test_scene_ordering(self):
        """Test scenes are ordered by scene_id."""
        Scene.objects.create(scene_id='03', title='Third', scene_type='story')
        Scene.objects.create(scene_id='01', title='First', scene_type='story')
        Scene.objects.create(scene_id='02', title='Second', scene_type='story')

        scenes = Scene.objects.all()
        self.assertEqual(scenes[0].scene_id, '01')
        self.assertEqual(scenes[1].scene_id, '02')
        self.assertEqual(scenes[2].scene_id, '03')

    def test_scene_types(self):
        """Test scene type choices."""
        scene = Scene.objects.create(
            scene_id='E1',
            title='Happy Ending',
            scene_type='ending',
            is_ending=True
        )
        self.assertEqual(scene.scene_type, 'ending')
        self.assertTrue(scene.is_ending)

    def test_scene_string_representation(self):
        """Test scene __str__ method."""
        scene = Scene.objects.create(
            scene_id='01',
            title='Test Scene',
            scene_type='story'
        )
        self.assertEqual(str(scene), '01: Test Scene')


class ChoiceModelTestCase(TestCase):
    """Test Choice model."""

    def setUp(self):
        self.scene1 = Scene.objects.create(scene_id='01', title='Start', scene_type='story')
        self.scene2 = Scene.objects.create(scene_id='02', title='Next', scene_type='story')

    def test_create_choice(self):
        """Test creating a choice between scenes."""
        choice = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Go forward',
            choice_letter='A',
            order=1
        )
        self.assertEqual(choice.from_scene, self.scene1)
        self.assertEqual(choice.to_scene, self.scene2)
        self.assertEqual(choice.choice_letter, 'A')

    def test_choice_foreign_keys(self):
        """Test choice foreign key relationships."""
        choice = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Test',
            choice_letter='A'
        )
        self.assertEqual(self.scene1.choices_from.first(), choice)
        self.assertEqual(self.scene2.choices_to.first(), choice)

    def test_choice_unique_together(self):
        """Test that from_scene + choice_letter must be unique."""
        Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='First',
            choice_letter='A'
        )
        with self.assertRaises(IntegrityError):
            Choice.objects.create(
                from_scene=self.scene1,
                to_scene=self.scene2,
                choice_text='Duplicate',
                choice_letter='A'
            )

    def test_choice_ordering(self):
        """Test choices are ordered by order field."""
        Choice.objects.create(from_scene=self.scene1, to_scene=self.scene2,
                            choice_text='Third', choice_letter='C', order=3)
        Choice.objects.create(from_scene=self.scene1, to_scene=self.scene2,
                            choice_text='First', choice_letter='A', order=1)
        Choice.objects.create(from_scene=self.scene1, to_scene=self.scene2,
                            choice_text='Second', choice_letter='B', order=2)

        choices = self.scene1.choices_from.all()
        self.assertEqual(choices[0].choice_letter, 'A')
        self.assertEqual(choices[1].choice_letter, 'B')
        self.assertEqual(choices[2].choice_letter, 'C')

    def test_choice_with_item_requirement(self):
        """Test choice can require an item."""
        item = Item.objects.create(
            item_id='ITEM_001',
            name='Key',
            description='A rusty key',
            found_in_scene=self.scene1
        )
        choice = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Unlock door',
            choice_letter='B',
            requires_item=item
        )
        self.assertEqual(choice.requires_item, item)


class ItemModelTestCase(TestCase):
    """Test Item model."""

    def setUp(self):
        self.scene = Scene.objects.create(scene_id='01', title='Start', scene_type='story')

    def test_create_item(self):
        """Test creating an item."""
        item = Item.objects.create(
            item_id='ITEM_001',
            name='Magic Spectacles',
            description='Reveals invisible ink',
            found_in_scene=self.scene,
            is_critical=True
        )
        self.assertEqual(item.item_id, 'ITEM_001')
        self.assertEqual(item.name, 'Magic Spectacles')
        self.assertTrue(item.is_critical)

    def test_item_found_in_relationship(self):
        """Test item's relationship with scene."""
        item = Item.objects.create(
            item_id='ITEM_001',
            name='Key',
            description='Test',
            found_in_scene=self.scene
        )
        self.assertIn(item, self.scene.items_here.all())

    def test_item_flags(self):
        """Test item boolean flags."""
        item = Item.objects.create(
            item_id='ITEM_002',
            name='Potion',
            description='Healing potion',
            found_in_scene=self.scene,
            is_critical=False,
            is_consumable=True,
            is_trap=False
        )
        self.assertFalse(item.is_critical)
        self.assertTrue(item.is_consumable)
        self.assertFalse(item.is_trap)


class GameStateModelTestCase(TestCase):
    """Test GameState model."""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.scene = Scene.objects.create(scene_id='01', title='Start', scene_type='story')

    def test_create_game_state(self):
        """Test creating a game state."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene
        )
        self.assertEqual(game_state.user, self.user)
        self.assertEqual(game_state.current_scene, self.scene)
        self.assertEqual(game_state.inventory, [])
        self.assertEqual(game_state.visited_scenes, [])
        self.assertEqual(game_state.flags, {})

    def test_game_state_inventory_methods(self):
        """Test inventory management methods."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene
        )

        # Test has_item when empty
        self.assertFalse(game_state.has_item('ITEM_001'))

        # Test add_item
        game_state.add_item('ITEM_001')
        self.assertTrue(game_state.has_item('ITEM_001'))
        self.assertEqual(game_state.items_collected, 1)

        # Test add_item prevents duplicates
        game_state.add_item('ITEM_001')
        self.assertEqual(len(game_state.inventory), 1)
        self.assertEqual(game_state.items_collected, 1)

    def test_game_state_flags(self):
        """Test flags JSON field."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene,
            flags={'dragon_befriended': True, 'chaos_level': 5}
        )
        self.assertTrue(game_state.flags['dragon_befriended'])
        self.assertEqual(game_state.flags['chaos_level'], 5)

    def test_game_state_stats(self):
        """Test game statistics tracking."""
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene
        )
        self.assertEqual(game_state.choices_made, 0)
        self.assertEqual(game_state.deaths, 0)
        self.assertEqual(game_state.items_collected, 0)

    def test_game_state_user_vs_session(self):
        """Test game state can use user or session."""
        # With user
        game_state1 = GameState.objects.create(
            user=self.user,
            current_scene=self.scene
        )
        self.assertIsNotNone(game_state1.user)
        self.assertIsNone(game_state1.session_key)

        # With session
        game_state2 = GameState.objects.create(
            session_key='abc123',
            current_scene=self.scene
        )
        self.assertIsNone(game_state2.user)
        self.assertIsNotNone(game_state2.session_key)


class EndingModelTestCase(TestCase):
    """Test Ending model."""

    def test_create_ending(self):
        """Test creating an ending."""
        ending = Ending.objects.create(
            ending_id='E1',
            title='Heroic Rescue',
            description='You saved the princess!',
            ending_type='victory',
            icon='⭐',
            achievement_text='The classic ending'
        )
        self.assertEqual(ending.ending_id, 'E1')
        self.assertEqual(ending.ending_type, 'victory')
        self.assertFalse(ending.is_secret)

    def test_ending_requirements(self):
        """Test ending requirements JSON field."""
        ending = Ending.objects.create(
            ending_id='E3',
            title='Test',
            description='Test',
            ending_type='victory',
            requirements={'items': ['ITEM_001', 'ITEM_002'], 'flags': {'npc_relations': '>0'}}
        )
        self.assertIn('ITEM_001', ending.requirements['items'])


class EndingUnlockModelTestCase(TestCase):
    """Test EndingUnlock model."""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.ending = Ending.objects.create(
            ending_id='E1',
            title='Test',
            description='Test',
            ending_type='victory'
        )

    def test_create_ending_unlock(self):
        """Test recording an ending unlock."""
        unlock = EndingUnlock.objects.create(
            user=self.user,
            ending=self.ending
        )
        self.assertEqual(unlock.user, self.user)
        self.assertEqual(unlock.ending, self.ending)

    def test_ending_unlock_unique_together(self):
        """Test user + ending must be unique."""
        EndingUnlock.objects.create(user=self.user, ending=self.ending)
        with self.assertRaises(IntegrityError):
            EndingUnlock.objects.create(user=self.user, ending=self.ending)
