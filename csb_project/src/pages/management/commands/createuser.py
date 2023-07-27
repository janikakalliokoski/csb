# csb_project/src/pages/management/commands/createuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']

        # Create a new user with hashed password
        new_user = User(username=username)
        new_user.set_password(password)

        # Save the user to the database
        new_user.save()

        self.stdout.write(self.style.SUCCESS(f'created user: {username}'))
