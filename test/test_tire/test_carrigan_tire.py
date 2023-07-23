import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):

    def test_needs_service(self):
        sensor_reports = [0.1, 0.9, 0.8, 0.4]
        tire = CarriganTire(sensor_reports)
        self.assertTrue(tire.needs_service())

    def test_needs_no_service(self):
        sensor_reports = [0.1, 0.6, 0.8, 0.4]
        tire = CarriganTire(sensor_reports)
        self.assertFalse(tire.needs_service())


