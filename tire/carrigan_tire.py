from tire.tire import Tire


class CarriganTire(Tire):

    def __int__(self, sensor_reports):
        self.sensor_reports = sensor_reports

    def needs_service(self):
        for tire_value in self.sensor_reports:
            if tire_value >= 0.9:
                return True
        return False
