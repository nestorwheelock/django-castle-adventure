"""
Management command to load all story content from fixtures.
"""
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load all story content from fixtures'

    def handle(self, *args, **options):
        self.stdout.write('Loading story content...')
        self.stdout.write('')

        self.stdout.write('Loading scenes...')
        call_command('loaddata', 'scenes', verbosity=0)
        self.stdout.write(self.style.SUCCESS('✓ Scenes loaded'))

        self.stdout.write('Loading items...')
        call_command('loaddata', 'items', verbosity=0)
        self.stdout.write(self.style.SUCCESS('✓ Items loaded'))

        self.stdout.write('Loading choices...')
        call_command('loaddata', 'choices', verbosity=0)
        self.stdout.write(self.style.SUCCESS('✓ Choices loaded'))

        self.stdout.write('Loading endings...')
        call_command('loaddata', 'endings', verbosity=0)
        self.stdout.write(self.style.SUCCESS('✓ Endings loaded'))

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Story content loaded successfully!'))
