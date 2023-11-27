from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'My command manage users'

    def add_arguments(self, parser):
        parser.add_argument('action', choices=['list', 'delete'],
                            help='Action to perform')
        parser.add_argument('--username', help='Username')
        parser.add_argument('--email', help='Email')
        parser.add_argument('--password', help='Password')

    def handle(self, *args, **options):
        action = options['action']
        

        if action == 'list':
            users = User.objects.all()
            self.stdout.write(f'Total users: {users.count()}')
            for user in users:
                self.stdout.write(f'User: {user.username}, Email: {user.email}')

        elif action == 'delete':
            username = options['username']
            try:
                user = User.objects.get(username=username)
                user.delete()
                self.stdout.write(f'Successfully deleted user {username}')
            except User.DoesNotExist:
                self.stderr.write(f'User {username} does not exist')
