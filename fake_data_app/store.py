from datetime import date
import numpy as np
from fake_data_app.sensor import VisitSensor




class StoreSensor:
    def __init__(
            self,
            name: str,
            avg_visit: int,
            std_visit: int,
            perc_malfunction: float = 0,
            perc_break: float = 0,
        ) -> None:
            """Initialize a store"""
            self.name = name
            self.sensors = list()

            # Keep consistent results for the same store
            seed = np.sum(list(self.name.encode("ascii")))
            np.random.seed(seed=seed)

            trafic_percentage = [0.48, 0.30, 0.05, 0.03, 0.01, 0.02, 0.1, 0.01]
            np.random.shuffle(trafic_percentage)

            # Initialize the store's sensors
            # Assumption: Each store has 8 sensors

            for i in range(8):
                sensor = VisitSensor(
                     trafic_percentage[i] * avg_visit,
                     trafic_percentage[i] * std_visit,
                     perc_malfunction,
                     perc_break,
                )
                self.sensors.append(sensor)
    
    # Get the trafic for one sensor at a specific date
    def get_sensor_trafic(self, sensor_id: int, business_date: date) -> int:
         return self.sensors[sensor_id].get_visit_count(business_date)
    
    # Get the traffic for all sensors of the store at a specific date
    def get_all_traffic(self, business_date: date) -> int:
        return sum([self.sensors[i].get_visit_count(business_date) for i in range(8)])
        