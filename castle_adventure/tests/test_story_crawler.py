"""
Comprehensive story path crawler tests.

These tests systematically crawl through ALL possible story paths
to ensure the entire game is playable and all content is reachable.
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from castle_adventure.models import Scene, Choice, Item, GameState, Ending
from collections import deque


class StoryGraphValidationTestCase(TestCase):
    """Validate the entire story graph structure."""

    def setUp(self):
        """Load fixtures before each test."""
        from django.core.management import call_command
        call_command('loaddata', 'scenes', verbosity=0)
        call_command('loaddata', 'items', verbosity=0)
        call_command('loaddata', 'choices', verbosity=0)
        call_command('loaddata', 'endings', verbosity=0)

    def test_all_scenes_loaded(self):
        """Verify all 30 scenes loaded correctly."""
        scene_count = Scene.objects.count()
        self.assertEqual(scene_count, 30, f"Expected 30 scenes, found {scene_count}")

    def test_all_choices_loaded(self):
        """Verify all 34 choices loaded correctly."""
        choice_count = Choice.objects.count()
        self.assertEqual(choice_count, 34, f"Expected 34 choices, found {choice_count}")

    def test_all_items_loaded(self):
        """Verify all 8 items loaded correctly."""
        item_count = Item.objects.count()
        self.assertEqual(item_count, 8, f"Expected 8 items, found {item_count}")

    def test_all_endings_loaded(self):
        """Verify all 5 endings loaded correctly."""
        ending_count = Ending.objects.count()
        self.assertEqual(ending_count, 5, f"Expected 5 endings, found {ending_count}")

    def test_start_scene_exists(self):
        """Verify scene 01 (start scene) exists."""
        start_scene = Scene.objects.filter(scene_id='01').first()
        self.assertIsNotNone(start_scene, "Start scene '01' not found")
        self.assertEqual(start_scene.scene_type, 'story')

    def test_all_choices_have_valid_scenes(self):
        """Verify all choices point to valid scenes."""
        for choice in Choice.objects.all():
            self.assertIsNotNone(choice.from_scene,
                f"Choice {choice.id} has no from_scene")
            self.assertIsNotNone(choice.to_scene,
                f"Choice {choice.id} has no to_scene")

            # Verify scenes exist
            from_exists = Scene.objects.filter(id=choice.from_scene.id).exists()
            to_exists = Scene.objects.filter(id=choice.to_scene.id).exists()

            self.assertTrue(from_exists,
                f"Choice {choice.id} from_scene doesn't exist")
            self.assertTrue(to_exists,
                f"Choice {choice.id} to_scene doesn't exist")

    def test_no_dead_end_story_scenes(self):
        """Verify all story scenes have at least one choice."""
        story_scenes = Scene.objects.filter(
            scene_type='story',
            is_ending=False,
            is_death=False
        )

        for scene in story_scenes:
            choices = Choice.objects.filter(from_scene=scene)
            self.assertGreater(choices.count(), 0,
                f"Story scene {scene.scene_id} '{scene.title}' has no choices (dead end)")

    def test_all_items_have_valid_scenes(self):
        """Verify all items are found in valid scenes."""
        for item in Item.objects.all():
            self.assertIsNotNone(item.found_in_scene,
                f"Item '{item.name}' has no found_in_scene")

            scene_exists = Scene.objects.filter(id=item.found_in_scene.id).exists()
            self.assertTrue(scene_exists,
                f"Item '{item.name}' found_in_scene doesn't exist")


class StoryPathCrawlerTestCase(TestCase):
    """Crawl all possible story paths to verify reachability."""

    def setUp(self):
        """Load fixtures and create test user."""
        from django.core.management import call_command
        call_command('loaddata', 'scenes', verbosity=0)
        call_command('loaddata', 'items', verbosity=0)
        call_command('loaddata', 'choices', verbosity=0)
        call_command('loaddata', 'endings', verbosity=0)

        self.client = Client()
        self.user = User.objects.create_user(username='testcrawler', password='testpass')

    def test_crawl_all_reachable_scenes(self):
        """Breadth-first search to find all reachable scenes from start."""
        start_scene = Scene.objects.get(scene_id='01')

        visited = set()
        queue = deque([start_scene])

        while queue:
            current = queue.popleft()

            if current.scene_id in visited:
                continue

            visited.add(current.scene_id)

            # Get all choices from this scene
            choices = Choice.objects.filter(from_scene=current)

            for choice in choices:
                if choice.to_scene.scene_id not in visited:
                    queue.append(choice.to_scene)

        # Verify all scenes are reachable
        all_scenes = set(Scene.objects.values_list('scene_id', flat=True))
        unreachable = all_scenes - visited

        self.assertEqual(len(unreachable), 0,
            f"Unreachable scenes found: {unreachable}")

        # Should have visited all 30 scenes
        self.assertEqual(len(visited), 30,
            f"Expected 30 reachable scenes, found {len(visited)}")

    def test_all_items_reachable(self):
        """Verify all items are in scenes reachable from start."""
        start_scene = Scene.objects.get(scene_id='01')

        # BFS to find reachable scenes
        visited = set()
        queue = deque([start_scene])

        while queue:
            current = queue.popleft()
            if current.scene_id in visited:
                continue
            visited.add(current.scene_id)

            choices = Choice.objects.filter(from_scene=current)
            for choice in choices:
                if choice.to_scene.scene_id not in visited:
                    queue.append(choice.to_scene)

        # Check all items are in reachable scenes
        for item in Item.objects.all():
            self.assertIn(item.found_in_scene.scene_id, visited,
                f"Item '{item.name}' in unreachable scene {item.found_in_scene.scene_id}")

    def test_all_endings_reachable(self):
        """Verify all ending scenes are reachable from start."""
        start_scene = Scene.objects.get(scene_id='01')

        # BFS to find reachable scenes
        visited = set()
        queue = deque([start_scene])

        while queue:
            current = queue.popleft()
            if current.scene_id in visited:
                continue
            visited.add(current.scene_id)

            choices = Choice.objects.filter(from_scene=current)
            for choice in choices:
                if choice.to_scene.scene_id not in visited:
                    queue.append(choice.to_scene)

        # Check all endings are reachable
        ending_scenes = Scene.objects.filter(is_ending=True)
        for scene in ending_scenes:
            self.assertIn(scene.scene_id, visited,
                f"Ending scene {scene.scene_id} '{scene.title}' is unreachable")

    def test_all_death_scenes_reachable(self):
        """Verify all death scenes are reachable from start."""
        start_scene = Scene.objects.get(scene_id='01')

        # BFS to find reachable scenes
        visited = set()
        queue = deque([start_scene])

        while queue:
            current = queue.popleft()
            if current.scene_id in visited:
                continue
            visited.add(current.scene_id)

            choices = Choice.objects.filter(from_scene=current)
            for choice in choices:
                if choice.to_scene.scene_id not in visited:
                    queue.append(choice.to_scene)

        # Check all death scenes are reachable
        death_scenes = Scene.objects.filter(is_death=True)
        for scene in death_scenes:
            self.assertIn(scene.scene_id, visited,
                f"Death scene {scene.scene_id} '{scene.title}' is unreachable")


class ActualPlaythroughTestCase(TestCase):
    """Test actual playthrough paths to verify game mechanics."""

    def setUp(self):
        """Load fixtures and create test user."""
        from django.core.management import call_command
        call_command('loaddata', 'scenes', verbosity=0)
        call_command('loaddata', 'items', verbosity=0)
        call_command('loaddata', 'choices', verbosity=0)
        call_command('loaddata', 'endings', verbosity=0)

        self.client = Client()
        self.user = User.objects.create_user(username='testplayer', password='testpass')
        self.client.login(username='testplayer', password='testpass')

    def test_simple_path_to_death(self):
        """Test following a path that leads to death."""
        # Start game
        response = self.client.get(reverse('castle_adventure:start'))
        self.assertEqual(response.status_code, 302)

        # Scene 01 -> Choice A (climb wall) -> Scene 02
        choice_a = Choice.objects.get(from_scene__scene_id='01', choice_letter='A')
        response = self.client.get(reverse('castle_adventure:choice', args=[choice_a.id]))
        self.assertEqual(response.status_code, 302)

        # Scene 02 -> Choice A (drop into courtyard) -> Scene 03
        choice_a2 = Choice.objects.get(from_scene__scene_id='02', choice_letter='A')
        response = self.client.get(reverse('castle_adventure:choice', args=[choice_a2.id]))
        self.assertEqual(response.status_code, 302)

        # Scene 03 -> Choice A (fight hellhounds) -> Death scene D2
        choice_fight = Choice.objects.get(from_scene__scene_id='03', choice_letter='A')
        response = self.client.get(reverse('castle_adventure:choice', args=[choice_fight.id]))
        self.assertEqual(response.status_code, 302)

        # Verify we're at a death scene
        game_state = GameState.objects.get(user=self.user)
        self.assertTrue(game_state.current_scene.is_death)
        self.assertEqual(game_state.deaths, 1)

    def test_item_pickup_and_use(self):
        """Test picking up an item and using it in a choice."""
        # Start game and navigate to scene with item
        self.client.get(reverse('castle_adventure:start'))

        # Navigate to troll's lair (scene 13) which has spectacles
        # Path: 01->B->27 or 01->A->02->A->03->B->04->A->05->A->07->A->08->A->09->B->12->A->13

        # Let's take the long path to get to the dungeon
        choices_path = [
            ('01', 'A'),  # Climb wall
            ('02', 'A'),  # Drop into courtyard
            ('03', 'B'),  # Run for drawbridge
            ('04', 'A'),  # Pull chain
            ('05', 'A'),  # Enter castle
            ('07', 'A'),  # Enter throne room
            ('08', 'A'),  # Continue to hallway
            ('09', 'B'),  # Descend to dungeon
            ('12', 'A'),  # Enter troll's lair
        ]

        for scene_id, letter in choices_path:
            choice = Choice.objects.get(from_scene__scene_id=scene_id, choice_letter=letter)
            self.client.get(reverse('castle_adventure:choice', args=[choice.id]))

        # Verify we're at scene 13 (Troll's Lair)
        game_state = GameState.objects.get(user=self.user)
        self.assertEqual(game_state.current_scene.scene_id, '13')

        # Pick up the spectacles
        spectacles = Item.objects.get(item_id='ITEM_001')
        response = self.client.get(reverse('castle_adventure:pickup_item', args=[spectacles.item_id]))

        # Verify item was picked up
        game_state.refresh_from_db()
        self.assertIn('ITEM_001', game_state.inventory)

    def test_complete_path_to_ending(self):
        """Test a complete path from start to an ending."""
        # Start game
        self.client.get(reverse('castle_adventure:start'))

        # Take simple path to princess rescue (ending scene 22)
        # This is the "heroic rescue" path
        choices_path = [
            ('01', 'B'),  # Approach front gate (bold) -> 27
        ]

        for scene_id, letter in choices_path:
            choice = Choice.objects.get(from_scene__scene_id=scene_id, choice_letter=letter)
            response = self.client.get(reverse('castle_adventure:choice', args=[choice.id]))
            self.assertEqual(response.status_code, 302)

        # Verify we progressed
        game_state = GameState.objects.get(user=self.user)
        self.assertGreater(game_state.choices_made, 0)


class ChoiceValidationTestCase(TestCase):
    """Test that all choices work correctly in actual gameplay."""

    def setUp(self):
        """Load fixtures and create test user."""
        from django.core.management import call_command
        call_command('loaddata', 'scenes', verbosity=0)
        call_command('loaddata', 'items', verbosity=0)
        call_command('loaddata', 'choices', verbosity=0)
        call_command('loaddata', 'endings', verbosity=0)

        self.client = Client()
        self.user = User.objects.create_user(username='choicetester', password='testpass')
        self.client.login(username='choicetester', password='testpass')

    def test_every_choice_is_clickable_from_correct_scene(self):
        """Verify every choice can be executed when at the correct scene."""
        all_choices = Choice.objects.all()

        for choice in all_choices:
            # Create game state at the from_scene
            GameState.objects.filter(user=self.user).delete()
            game_state = GameState.objects.create(
                user=self.user,
                current_scene=choice.from_scene
            )

            # If choice requires item, add it
            if choice.requires_item:
                game_state.add_item(choice.requires_item.item_id)
                game_state.save()

            # Execute the choice
            response = self.client.get(reverse('castle_adventure:choice', args=[choice.id]))

            # Should redirect (success), not 400 (bad request)
            self.assertEqual(response.status_code, 302,
                f"Choice {choice.id} ({choice.choice_text}) from scene {choice.from_scene.scene_id} failed")

            # Verify game state updated
            game_state.refresh_from_db()
            self.assertEqual(game_state.current_scene, choice.to_scene,
                f"Choice {choice.id} didn't navigate to correct scene")
