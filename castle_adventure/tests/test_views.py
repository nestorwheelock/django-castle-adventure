"""
Tests for scene navigation views (T-003).
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from castle_adventure.models import Scene, Choice, Item, GameState


class StartGameViewTestCase(TestCase):
    """Tests for start_game view."""

    def setUp(self):
        self.client = Client()
        self.start_scene = Scene.objects.create(
            scene_id='01',
            title='Castle Entrance',
            description='You stand before a dark castle.',
            scene_type='story'
        )

    def test_start_new_game_creates_game_state(self):
        """Test that starting a new game creates GameState."""
        response = self.client.get(reverse('castle_adventure:start'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(GameState.objects.filter(current_scene=self.start_scene).exists())

    def test_start_game_with_authenticated_user(self):
        """Test game state uses user FK when authenticated."""
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('castle_adventure:start'))

        game_state = GameState.objects.get(user=user)
        self.assertEqual(game_state.current_scene, self.start_scene)
        self.assertIsNone(game_state.session_key)

    def test_start_game_with_anonymous_user(self):
        """Test game state uses session_key when anonymous."""
        response = self.client.get(reverse('castle_adventure:start'))

        game_state = GameState.objects.first()
        self.assertIsNone(game_state.user)
        self.assertIsNotNone(game_state.session_key)


class DisplaySceneViewTestCase(TestCase):
    """Tests for display_scene view."""

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
            choice_text='Enter the hall',
            choice_letter='A',
            order=1
        )

    def test_display_scene_shows_scene(self):
        """Test that display_scene renders scene."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.get(reverse('castle_adventure:scene', args=['01']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dark entrance')

    def test_display_scene_shows_choices(self):
        """Test that available choices are displayed."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.get(reverse('castle_adventure:scene', args=['01']))
        self.assertContains(response, 'Enter the hall')

    def test_display_scene_filters_locked_choices(self):
        """Test that choices requiring items are marked as locked."""
        self.client.login(username='testuser', password='testpass')

        key = Item.objects.create(
            item_id='key',
            name='Rusty Key',
            description='Opens doors',
            found_in_scene=self.scene1
        )

        locked_choice = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Unlock door',
            choice_letter='B',
            requires_item=key,
            order=2
        )

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.get(reverse('castle_adventure:scene', args=['01']))
        choices = response.context['choices']

        locked = [c for c in choices if c.choice_letter == 'B'][0]
        self.assertTrue(locked.is_locked)


class MakeChoiceViewTestCase(TestCase):
    """Tests for make_choice view."""

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
        self.death_scene = Scene.objects.create(
            scene_id='D1',
            title='Death',
            description='You died',
            scene_type='death',
            is_death=True
        )

        self.choice1 = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Enter the hall',
            choice_letter='A',
            order=1
        )

    def test_make_valid_choice_navigates(self):
        """Test making a valid choice navigates to next scene."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))
        self.assertEqual(response.status_code, 302)

        game_state.refresh_from_db()
        self.assertEqual(game_state.current_scene, self.scene2)

    def test_make_choice_updates_stats(self):
        """Test that making choice updates game state stats."""
        self.client.login(username='testuser', password='testpass')
        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))

        game_state.refresh_from_db()
        self.assertEqual(game_state.choices_made, 1)
        self.assertIn('02', game_state.visited_scenes)

    def test_make_choice_invalid_scene(self):
        """Test that choice from wrong scene is rejected."""
        self.client.login(username='testuser', password='testpass')

        other_scene = Scene.objects.create(
            scene_id='03',
            title='Other',
            description='Other room',
            scene_type='story'
        )

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=other_scene
        )

        response = self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))
        self.assertEqual(response.status_code, 400)

    def test_make_choice_missing_required_item(self):
        """Test that choice requiring item is rejected without item."""
        self.client.login(username='testuser', password='testpass')

        key = Item.objects.create(
            item_id='key',
            name='Rusty Key',
            description='Opens doors',
            found_in_scene=self.scene1
        )

        locked_choice = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Unlock door',
            choice_letter='B',
            requires_item=key,
            order=2
        )

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        response = self.client.post(reverse('castle_adventure:choice', args=[locked_choice.id]))
        self.assertEqual(response.status_code, 400)

    def test_make_choice_increments_deaths(self):
        """Test that death scenes increment death counter."""
        self.client.login(username='testuser', password='testpass')

        death_choice = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.death_scene,
            choice_text='Jump off cliff',
            choice_letter='C',
            order=3
        )

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        self.client.post(reverse('castle_adventure:choice', args=[death_choice.id]))

        game_state.refresh_from_db()
        self.assertEqual(game_state.deaths, 1)


class HelperFunctionsTestCase(TestCase):
    """Tests for helper functions."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.start_scene = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )

    def test_get_or_create_authenticated_user(self):
        """Test get_or_create_game_state for authenticated user."""
        from castle_adventure.views import get_or_create_game_state
        from django.test import RequestFactory

        factory = RequestFactory()
        request = factory.get('/fake/')
        request.user = self.user
        request.session = self.client.session

        result = get_or_create_game_state(request)
        self.assertIsNone(result)

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.start_scene
        )

        result = get_or_create_game_state(request)
        self.assertEqual(result, game_state)

    def test_get_or_create_anonymous_user(self):
        """Test get_or_create_game_state for anonymous user."""
        from castle_adventure.views import get_or_create_game_state
        from django.test import RequestFactory
        from django.contrib.auth.models import AnonymousUser

        factory = RequestFactory()
        request = factory.get('/fake/')
        request.user = AnonymousUser()
        request.session = self.client.session

        result = get_or_create_game_state(request)
        self.assertIsNone(result)


class IntegrationTestCase(TestCase):
    """Integration tests for full navigation flow."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Entrance',
            description='Castle entrance',
            scene_type='story'
        )
        self.scene2 = Scene.objects.create(
            scene_id='02',
            title='Hall',
            description='Grand hall',
            scene_type='story'
        )
        self.scene3 = Scene.objects.create(
            scene_id='03',
            title='Throne Room',
            description='Royal throne',
            scene_type='story'
        )

        self.choice1 = Choice.objects.create(
            from_scene=self.scene1,
            to_scene=self.scene2,
            choice_text='Enter hall',
            choice_letter='A'
        )
        self.choice2 = Choice.objects.create(
            from_scene=self.scene2,
            to_scene=self.scene3,
            choice_text='Approach throne',
            choice_letter='A'
        )

    def test_full_navigation_flow(self):
        """Test start -> scene -> choice -> next scene flow."""
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(reverse('castle_adventure:start'))
        self.assertEqual(response.status_code, 302)

        game_state = GameState.objects.get(user=self.user)
        self.assertEqual(game_state.current_scene.scene_id, '01')

        response = self.client.get(reverse('castle_adventure:scene', args=['01']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Castle entrance')

        response = self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))
        self.assertEqual(response.status_code, 302)

        game_state.refresh_from_db()
        self.assertEqual(game_state.current_scene.scene_id, '02')
        self.assertEqual(game_state.choices_made, 1)

    def test_multi_step_navigation(self):
        """Test navigating through multiple scenes."""
        self.client.login(username='testuser', password='testpass')

        self.client.get(reverse('castle_adventure:start'))
        self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))
        self.client.post(reverse('castle_adventure:choice', args=[self.choice2.id]))

        game_state = GameState.objects.get(user=self.user)
        self.assertEqual(game_state.current_scene.scene_id, '03')
        self.assertEqual(game_state.choices_made, 2)
        self.assertIn('02', game_state.visited_scenes)
        self.assertIn('03', game_state.visited_scenes)

    def test_visited_scenes_tracking(self):
        """Test that visited scenes are tracked correctly."""
        self.client.login(username='testuser', password='testpass')

        self.client.get(reverse('castle_adventure:start'))
        game_state = GameState.objects.get(user=self.user)

        self.client.post(reverse('castle_adventure:choice', args=[self.choice1.id]))
        game_state.refresh_from_db()

        self.assertIn('02', game_state.visited_scenes)
        self.assertEqual(len(game_state.visited_scenes), 1)
