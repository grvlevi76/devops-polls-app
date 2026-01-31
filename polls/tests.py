from django.test import TestCase
from django.urls import reverse

class BasicTest(TestCase):
    def test_homepage(self):
        """
        A basic test to ensure the homepage or polls index returns a 200 status code.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
