from django.core.management.base import BaseCommand
from lesson2.models import User


class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user id')

    def handle(self, *args, **kwargs):
        find_id = kwargs['pk']
        user = User.objects.filter(pk=find_id).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')
