from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import *

class TestBaseUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
