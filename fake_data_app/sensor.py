from datetime import date, timedelta
import sys

import numpy as np


class VisitSensor:

    def __init__(
            self,
            avg_visit: int,
            std_visit: int,
            perc_break: float = 0.015,
            perc_malfunction : float = 0.035
        ) -> None:
        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_malfunction = perc_malfunction
        self.perc_break = perc_break
    

    def simulate_visit_count(self, business_date: date) -> int:
        
        np.random.seed(seed=business_date.toordinal())

        week_day = business_date.weekday()

        visit = np.random.normal(self.avg_visit, self.std_visit)

        if week_day == 2:
            visit *= 1.10
        if week_day == 4:
            visit *= 1.25
        if week_day == 5:
            visit *= 1.35
        
        # store closed on sunday
        if week_day == 6:
            visit = -1
        
        return np.floor(visit)
    
    def get_visit_count(self, business_date: date) -> int:
        """returns the number of the persons detected by the sensor during the day"""

        np.random.seed(seed=business_date.toordinal())
        proba_malfunction = np.random.random()

        #the sensor can break sometimes
        if proba_malfunction < self.perc_break:
            print("break")
            return 0
        
        visit = self.simulate_visit_count(business_date)

        # The sensor can also malfunction
        if proba_malfunction < self.perc_malfunction:
            print("malfunction")
            visit = np.floor(visit * 0.2) # make it so bad we can detect it!
        
        return visit



if __name__ == "__main__":
    if len(sys.argv) > 1:
        year, month, day = [int(v) for v in sys.argv[1].split("-")]
    else:
        year, month, day = 2024, 8, 29
    queried_date = date(year, month, day)

    capteur = VisitSensor(avg_visit=1500, std_visit=150)
    capteur2 = VisitSensor(avg_visit=2000, std_visit=200)
    print(capteur.get_visit_count(queried_date))
    print(capteur2.get_visit_count(queried_date))
    


