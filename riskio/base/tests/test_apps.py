from django.apps import apps
from base.apps import BaseConfig
from django.test import TestCase

class BaseConfigTest(TestCase):
    def test_base_app(self):
        self.assertEqual(BaseConfig.name, 'base')
        self.assertEqual(apps.get_app_config('base').name, 'base')
