from django.test import TestCase
from .models import Experiment
from .views import calculate_average_value

class DataAnalysisTestCase(TestCase):
    def setUp(self):
        # Set up test data
        Experiment.objects.create(name='Experiment 1', date='2024-05-01', observation_type='Type A', value=10.0)
        Experiment.objects.create(name='Experiment 1', date='2024-05-01', observation_type='Type A', value=20.0)
        Experiment.objects.create(name='Experiment 1', date='2024-05-01', observation_type='Type B', value=30.0)

    def test_calculate_average_value(self):
        # Test calculate_average_value function
        data = calculate_average_value()
        self.assertEqual(len(data), 1)
        self.assertIn('Experiment 1', data)
        self.assertEqual(len(data['Experiment 1']), 2)
        self.assertAlmostEqual(data['Experiment 1']['Type A']['average_value'], 15.0)
        self.assertAlmostEqual(data['Experiment 1']['Type B']['average_value'], 30.0)
