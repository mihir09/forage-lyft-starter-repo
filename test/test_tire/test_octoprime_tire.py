import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):

    def test_needs_service(self):
        sensor_reports = [0.8, 0.9, 0.8, 0.5]
        tire = OctoprimeTire(sensor_reports)
        self.assertTrue(tire.needs_service())

    def test_needs_no_service(self):
        sensor_reports = [0.1, 0.6, 0.8, 0.4]
        tire = OctoprimeTire(sensor_reports)
        self.assertFalse(tire.needs_service())