from django.test import TestCase, Client
from django.urls import reverse
from base.views import index

class BaseViewsTest(TestCase):
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
