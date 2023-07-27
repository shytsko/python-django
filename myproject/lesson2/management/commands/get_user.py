from django.core.management.base import BaseCommand
from lesson2.models import User


class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='user id')

    def handle(self, *args, **kwargs):
        find_id = kwargs['id']
        user = User.objects.get(id=find_id)
        self.stdout.write(f'{user}')
