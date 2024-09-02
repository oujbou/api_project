import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from fake_data_app.sensor import VisitSensor
import unittest
from datetime import date


class TestVisitSensor(unittest.TestCase):
    
    def test_monday_open(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300)
        visit_count = visit_sensor.simulate_visit_count(date(year=2023, month=9, day=11))

        self.assertFalse(visit_sensor == -1)
    
    def test_tuesday_open(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300)
        visit_count = visit_sensor.simulate_visit_count(date(year=2023, month=9, day=12))

        self.assertFalse(visit_count == -1)
    
    def test_wednesday_open(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300)
        visit_count = visit_sensor.simulate_visit_count(date(year=2023, month=9, day=13))

        self.assertFalse(visit_count == -1)
    
    def test_thirsday_open(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300)
        visit_count = visit_sensor.simulate_visit_count(date(year=2023, month=9, day=14))

        self.assertFalse(visit_count == -1)

    def test_friday_open(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300)
        visit_count = visit_sensor.simulate_visit_count(date(year=2023, month=9, day=15))

        self.assertFalse(visit_count == -1)
    
    def test_saturday_open(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300)
        visit_count = visit_sensor.simulate_visit_count(date(year=2023, month=9, day=16))

        self.assertFalse(visit_count == -1)
    
    def test_sunday_closed(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300)
        visit_count = visit_sensor.simulate_visit_count(date(year=2023, month=9, day=17))

        self.assertEqual(visit_count, -1)

    def test_with_break(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300, perc_break=10)
        visit_count = visit_sensor.get_visit_count(date(year=2023, month=10, day=22))

        self.assertEqual(visit_count, 0)

    def test_with_malfunction(self):
        visit_sensor = VisitSensor(avg_visit=1200, std_visit=300, perc_malfunction=10)
        visit_count = visit_sensor.get_visit_count(date(year=2023, month=11, day=28))

        self.assertEqual(visit_count, 238)
    
if __name__ == '__main__':
    unittest.main()