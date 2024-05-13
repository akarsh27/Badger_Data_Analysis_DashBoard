from django.test import TestCase, Client
from django.urls import reverse

class DataIngestionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_upload_csv_valid_data(self):
        with open('/Users/akarshache/Downloads/experiment_data - Sheet1.csv', 'rb') as file:
            response = self.client.post(reverse('upload_csv'), {'file': file})
        self.assertEqual(response.status_code, 302) 
