from tire.tire import Tire


class OctoprimeTire(Tire):

    def __int__(self, sensor_reports):
        self.sensor_reports = sensor_reports

    def needs_service(self):
        return sum(self.sensor_reports) >= 3
