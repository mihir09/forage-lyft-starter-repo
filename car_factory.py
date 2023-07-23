from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine
from car import Car

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(capulet_engine.CapuletEngine(current_mileage, last_service_mileage), spindler_battery.SpindlerBattery(current_date, last_service_date))

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage), spindler_battery.SpindlerBattery(current_date, last_service_date))

    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        return Car(sternman_engine.SternmanEngine(warning_light_is_on), spindler_battery.SpindlerBattery(current_date, last_service_date))

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage), nubbin_battery.NubbinBattery(current_date, last_service_date))

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(capulet_engine.CapuletEngine(current_mileage, last_service_mileage), nubbin_battery.NubbinBattery(current_date, last_service_date))
