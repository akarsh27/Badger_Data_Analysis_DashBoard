from django.test import TestCase, Client
from django.urls import reverse

class DataPresentationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_data_page_loads(self):
        response = self.client.get(reverse('display_data'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Experiment Data Analysis') 
