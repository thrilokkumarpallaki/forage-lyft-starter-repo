from datetime import date

from model import Calliope
from model import Glissade
from model import Palindrome
from model import Rorschach
from model import Thovex

from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine

from battery import NubbinBattery
from battery import SpindlerBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Calliope:
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        car = Calliope(capulet_engine, spindler_battery)
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Glissade:
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        car = Glissade(willoughby_engine, spindler_battery)
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Palindrome:
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        car = Palindrome(sternman_engine, spindler_battery)
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int) -> Rorschach:
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        car = Rorschach(willoughby_engine, nubbin_battery)
        return car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int) -> Thovex:
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        car = Thovex(capulet_engine, nubbin_battery)
        return car
