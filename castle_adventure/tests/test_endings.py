"""
Tests for ending determination and unlock system (T-006).
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from castle_adventure.models import Scene, Ending, EndingUnlock, GameState


class DetermineEndingTestCase(TestCase):
    """Tests for determine_ending logic."""

    def setUp(self):
        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )

        self.user = User.objects.create_user(username='testuser', password='testpass')

        Ending.objects.create(
            ending_id='E1',
            title='Heroic Rescue',
            description='You rescued the princess',
            ending_type='victory',
            icon='👑'
        )
        Ending.objects.create(
            ending_id='E2',
            title='Tragic Betrayal',
            description='You betrayed everyone',
            ending_type='betrayal',
            icon='🗡️'
        )
        Ending.objects.create(
            ending_id='E3',
            title='Mutual Escape',
            description='Everyone escaped together',
            ending_type='victory',
            icon='🚪'
        )
        Ending.objects.create(
            ending_id='E4',
            title='Castle Collapse',
            description='The castle collapsed',
            ending_type='defeat',
            icon='💥'
        )
        Ending.objects.create(
            ending_id='E5',
            title='True King',
            description='You became the true king',
            ending_type='secret',
            icon='👑',
            is_secret=True
        )

    def test_determine_ending_default_heroic_rescue(self):
        """Test default ending is Heroic Rescue (E1)."""
        from castle_adventure.ending_logic import determine_ending

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1
        )

        ending_id = determine_ending(game_state)
        self.assertEqual(ending_id, 'E1')

    def test_determine_ending_tragic_betrayal(self):
        """Test Tragic Betrayal (E2) when NPCs killed."""
        from castle_adventure.ending_logic import determine_ending

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            flags={'killed_npcs': True}
        )

        ending_id = determine_ending(game_state)
        self.assertEqual(ending_id, 'E2')

    def test_determine_ending_mutual_escape(self):
        """Test Mutual Escape (E3) when all NPCs befriended."""
        from castle_adventure.ending_logic import determine_ending

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            inventory=['ITEM_004'],
            flags={
                'dragon_befriended': True,
                'troll_befriended': True,
                'wizard_helped': True
            }
        )

        ending_id = determine_ending(game_state)
        self.assertEqual(ending_id, 'E3')

    def test_determine_ending_castle_collapse(self):
        """Test Castle Collapse (E4) when chaos too high."""
        from castle_adventure.ending_logic import determine_ending

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            flags={'chaos_level': 15}
        )

        ending_id = determine_ending(game_state)
        self.assertEqual(ending_id, 'E4')

    def test_determine_ending_secret_true_king(self):
        """Test True King (E5) with all requirements."""
        from castle_adventure.ending_logic import determine_ending

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            inventory=['ITEM_001', 'ITEM_002', 'ITEM_003', 'ITEM_004',
                      'ITEM_005', 'ITEM_006', 'ITEM_007', 'ITEM_008'],
            flags={
                'dragon_befriended': True,
                'troll_befriended': True,
                'wizard_helped': True,
                'sat_on_throne': True
            }
        )

        ending_id = determine_ending(game_state)
        self.assertEqual(ending_id, 'E5')


class EndingRequirementsTestCase(TestCase):
    """Tests for ending requirement checks."""

    def setUp(self):
        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_item_requirement_check(self):
        """Test ending requires specific items."""
        from castle_adventure.ending_logic import determine_ending

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            flags={
                'dragon_befriended': True,
                'troll_befriended': True,
                'wizard_helped': True
            }
        )

        ending_id = determine_ending(game_state)
        self.assertNotEqual(ending_id, 'E3')

    def test_flag_requirement_check(self):
        """Test ending requires specific flags."""
        from castle_adventure.ending_logic import determine_ending

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            inventory=['ITEM_004']
        )

        ending_id = determine_ending(game_state)
        self.assertNotEqual(ending_id, 'E3')

    def test_npc_relations_negative(self):
        """Test negative NPC relations triggers betrayal."""
        from castle_adventure.ending_logic import determine_ending

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.scene1,
            flags={'npc_relations': -5}
        )

        ending_id = determine_ending(game_state)
        self.assertEqual(ending_id, 'E2')


class UnlockEndingTestCase(TestCase):
    """Tests for ending unlock functionality."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='E1',
            title='Heroic Rescue',
            description='Victory ending',
            scene_type='ending',
            is_ending=True
        )

        self.ending1 = Ending.objects.create(
            ending_id='E1',
            title='Heroic Rescue',
            description='You rescued the princess',
            ending_type='victory',
            icon='👑',
            achievement_text='Rescued the princess'
        )

    def test_unlock_ending_for_authenticated_user(self):
        """Test ending unlock for authenticated user."""
        from castle_adventure.views import unlock_ending
        from django.test import RequestFactory

        factory = RequestFactory()
        request = factory.get('/fake/')
        request.user = self.user
        request.session = self.client.session

        unlock_ending(request, self.ending1)

        self.assertTrue(EndingUnlock.objects.filter(
            user=self.user,
            ending=self.ending1
        ).exists())

    def test_unlock_ending_for_anonymous_user(self):
        """Test ending unlock for anonymous user."""
        from castle_adventure.views import unlock_ending
        from django.test import RequestFactory
        from django.contrib.auth.models import AnonymousUser

        factory = RequestFactory()
        request = factory.get('/fake/')
        request.user = AnonymousUser()
        request.session = self.client.session
        request.session.create()

        unlock_ending(request, self.ending1)

        self.assertTrue(EndingUnlock.objects.filter(
            session_key=request.session.session_key,
            ending=self.ending1
        ).exists())


class GetUnlockedEndingsTestCase(TestCase):
    """Tests for retrieving unlocked endings."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.ending1 = Ending.objects.create(
            ending_id='E1',
            title='Heroic Rescue',
            description='Victory',
            ending_type='victory',
            icon='👑',
            achievement_text='Rescued'
        )
        self.ending2 = Ending.objects.create(
            ending_id='E2',
            title='Tragic Betrayal',
            description='Defeat',
            ending_type='betrayal',
            icon='🗡️',
            achievement_text='Betrayed'
        )

    def test_get_unlocked_endings_returns_correct_list(self):
        """Test get_unlocked_endings returns correct ending IDs."""
        from castle_adventure.views import get_unlocked_endings
        from django.test import RequestFactory

        EndingUnlock.objects.create(user=self.user, ending=self.ending1)

        factory = RequestFactory()
        request = factory.get('/fake/')
        request.user = self.user
        request.session = self.client.session

        unlocked = get_unlocked_endings(request)
        self.assertIn(self.ending1.id, unlocked)
        self.assertNotIn(self.ending2.id, unlocked)

    def test_get_unlocked_endings_empty_for_new_user(self):
        """Test get_unlocked_endings returns empty for new user."""
        from castle_adventure.views import get_unlocked_endings
        from django.test import RequestFactory

        factory = RequestFactory()
        request = factory.get('/fake/')
        request.user = self.user
        request.session = self.client.session

        unlocked = list(get_unlocked_endings(request))
        self.assertEqual(len(unlocked), 0)


class DisplayEndingViewTestCase(TestCase):
    """Tests for display_ending view."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )

        self.ending_scene = Scene.objects.create(
            scene_id='E1',
            title='Heroic Rescue',
            description='Victory ending',
            scene_type='ending',
            is_ending=True
        )

        self.ending1 = Ending.objects.create(
            ending_id='E1',
            title='Heroic Rescue',
            description='You rescued the princess',
            ending_type='victory',
            icon='👑',
            achievement_text='Rescued the princess'
        )

    def test_display_ending_shows_correct_ending(self):
        """Test display_ending shows correct ending based on game state."""
        self.client.login(username='testuser', password='testpass')

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.ending_scene
        )

        response = self.client.get(reverse('castle_adventure:display_ending', args=['E1']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Heroic Rescue')

    def test_display_ending_marks_game_complete(self):
        """Test display_ending marks game as complete."""
        self.client.login(username='testuser', password='testpass')

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.ending_scene
        )

        self.client.get(reverse('castle_adventure:display_ending', args=['E1']))

        game_state.refresh_from_db()
        self.assertTrue(game_state.is_complete)
        self.assertEqual(game_state.ending_reached, 'E1')


class EndingsCollectionViewTestCase(TestCase):
    """Tests for endings_collection view."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.ending1 = Ending.objects.create(
            ending_id='E1',
            title='Heroic Rescue',
            description='Victory',
            ending_type='victory',
            icon='👑',
            achievement_text='Rescued'
        )
        self.ending2 = Ending.objects.create(
            ending_id='E2',
            title='Tragic Betrayal',
            description='Defeat',
            ending_type='betrayal',
            icon='🗡️',
            achievement_text='Betrayed'
        )

    def test_endings_collection_shows_all_endings(self):
        """Test endings_collection displays all endings."""
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(reverse('castle_adventure:endings_collection'))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['endings']), 2)
        self.assertEqual(response.context['total_endings'], 2)

    def test_endings_collection_shows_locked_status(self):
        """Test endings_collection shows locked/unlocked status."""
        self.client.login(username='testuser', password='testpass')

        EndingUnlock.objects.create(user=self.user, ending=self.ending1)

        response = self.client.get(reverse('castle_adventure:endings_collection'))

        endings = list(response.context['endings'])
        unlocked_count = response.context['unlocked_count']

        self.assertEqual(unlocked_count, 1)


class EndingsIntegrationTestCase(TestCase):
    """Integration tests for full ending flow."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.scene1 = Scene.objects.create(
            scene_id='01',
            title='Start',
            description='Start scene',
            scene_type='story'
        )

        self.ending_scene = Scene.objects.create(
            scene_id='E1',
            title='Heroic Rescue',
            description='Victory ending',
            scene_type='ending',
            is_ending=True
        )

        self.ending1 = Ending.objects.create(
            ending_id='E1',
            title='Heroic Rescue',
            description='You rescued the princess',
            ending_type='victory',
            icon='👑',
            achievement_text='Rescued the princess'
        )

    def test_playthrough_to_ending_unlocks_achievement(self):
        """Test completing game unlocks ending achievement."""
        self.client.login(username='testuser', password='testpass')

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.ending_scene
        )

        self.client.get(reverse('castle_adventure:display_ending', args=['E1']))

        self.assertTrue(EndingUnlock.objects.filter(
            user=self.user,
            ending=self.ending1
        ).exists())

    def test_viewing_endings_collection_after_unlock(self):
        """Test endings collection shows progress after unlock."""
        self.client.login(username='testuser', password='testpass')

        game_state = GameState.objects.create(
            user=self.user,
            current_scene=self.ending_scene
        )

        self.client.get(reverse('castle_adventure:display_ending', args=['E1']))

        response = self.client.get(reverse('castle_adventure:endings_collection'))

        self.assertEqual(response.context['unlocked_count'], 1)
