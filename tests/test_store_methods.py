import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from datetime import date

from fake_data_app.store import StoreSensor


class TestStore(unittest.TestCase):
    def test_get_store_traffic(self):
        lille_sotre = StoreSensor(name="Lille", avg_visit=1200, std_visit=300)
        visits = lille_sotre.get_store_traffic(date(year=2024, month=8, day=26))
        self.assertEqual(visits, 902)

    def test_get_sensor_traffic(self):
        lille_store = StoreSensor(name="Lille", avg_visit=1200, std_visit=300)
        visits = lille_store.get_sensor_traffic(2, date(2024, 8, 27))
        self.assertEqual(visits, 33)

    def test_sunday_closed(self):
        lille_store = StoreSensor("Lille", 1200, 300)
        visits = lille_store.get_sensor_traffic(2, date(2024, 9, 1))
        self.assertEqual(visits, -1)


if __name__ == "__main__":
    unittest.main()
