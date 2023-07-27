from django.core.management.base import BaseCommand
from lesson2.models import User


class Command(BaseCommand):
    help = "Update user name"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user id')
        parser.add_argument('new_name', type=str, help='new user name')

    def handle(self, *args, **kwargs):
        find_id = kwargs['pk']
        user = User.objects.filter(pk=find_id).first()
        user.name = kwargs['new_name']
        user.save()
        self.stdout.write(f'{user}')
