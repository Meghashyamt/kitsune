from django.core.management.base import BaseCommand

from search.utils import es_whazzup


class Command(BaseCommand):
    help = 'Shows elastic stats.'

    def handle(self, *args, **options):
        es_whazzup()
