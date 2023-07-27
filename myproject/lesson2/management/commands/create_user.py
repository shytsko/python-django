from django.core.management.base import BaseCommand
from lesson2.models import User


class Command(BaseCommand):
    help = "Create new user"

    def handle(self, *args, **kwargs):
        new_user = User(name="user1", email="user1@mail.com", password="password", age=40)
        new_user.save()
        self.stdout.write(f'{new_user =}')
        new_user = User(name="user2", email="user2@mail.com", password="password", age=25)
        new_user.save()
        self.stdout.write(f'{new_user =}')
        new_user = User(name="user3", email="user3@mail.com", password="password", age=33)
        new_user.save()
        self.stdout.write(f'{new_user =}')
