from datetime import date

import numpy as np


class VisitSensor:

    def __init__(self, avg_visit: int, std_visit: int ) -> None:
        self.avg_visit = avg_visit
        self.std_visit = std_visit
    

    def simulate_visit(self, business_date: date) -> int:
        
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


if __name__ == "__main__":
    capteur = VisitSensor(avg_visit=1500, std_visit=150)
    print(capteur.simulate_visit(date(year=2024, month=8, day=29)))
    print(capteur.avg_visit)


