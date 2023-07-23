from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine
from tire import carrigan_tire, octoprime_tire
from car import Car


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_reports):
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date, last_service_date)
        tire = carrigan_tire.CarriganTire(sensor_reports)
        return Car(engine, battery, tire)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_reports):
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date, last_service_date)
        tire = carrigan_tire.CarriganTire(sensor_reports)
        return Car(engine, battery, tire)

    def create_palindrome(self, current_date, last_service_date, warning_light_is_on, sensor_reports):
        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(current_date, last_service_date)
        tire = carrigan_tire.CarriganTire(sensor_reports)
        return Car(engine, battery, tire)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_reports):
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date, last_service_date)
        tire = octoprime_tire.OctoprimeTire(sensor_reports)
        return Car(engine, battery, tire)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_reports):
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date, last_service_date)
        tire = octoprime_tire.OctoprimeTire(sensor_reports)
        return Car(engine, battery, tire)
