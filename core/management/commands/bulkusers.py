from django.core.management.base import BaseCommand

from people.models import SocialUser


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print self.args
        self.stdout.write('Starting to generate fake users.')
        users = []
        num = 100
        for i in range(num):
            user = SocialUser(first_name='User%dFirstName' %
                              i, last_name='User%dLastName' % i,
                              username='user%d' % i, email='user%ddomain.com' % i,
                              password='pbkdf2_sha256$12000$aI0u3RsnZhpN$4zmRadIbHQjbKR8ULRWOFQTO7mECglWtNjWa09+a1kg=',
                              is_active=True)
            users.append(user)
        SocialUser.objects.bulk_create(users)
        self.stdout.write('Saved %d users.' % num)
