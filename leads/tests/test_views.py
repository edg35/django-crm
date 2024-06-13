from django.shortcuts import reverse
from django.test import TestCase


class LandingPageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse("landing-page"))
        # Status Code is 200
        self.assertEqual(response.status_code, 200)
        # Correct template response
        self.assertTemplateUsed(response, "landing.html")
