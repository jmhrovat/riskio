from django.apps import apps
from users.apps import UsersConfig
from django.test import TestCase

class UsersConfigTest(TestCase):
    def test_users_app(self):
        self.assertEqual(UsersConfig.name, 'users')
        self.assertEqual(apps.get_app_config('users').name, 'users')
