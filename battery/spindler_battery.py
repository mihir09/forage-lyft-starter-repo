from battery.battery import Battery
from datetime import datetime
class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date) -> None:
        super(SpindlerBattery, self).__init__(current_date, last_service_date)

    def needs_service(self):
        predicted_service_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return predicted_service_date < datetime.today().date()