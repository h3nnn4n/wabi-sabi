from django.test import TestCase
from django.urls import reverse


class HealthViewTests(TestCase):
    def test_ok(self):
        """
        Simply test that the view returns 'ok'
        """
        response = self.client.get(reverse('health:index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'ok')
