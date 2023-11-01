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
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int, tire_values: list[float]) -> Calliope:
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        carrigan_tires = CarriganTire(tire_values)

        car = Calliope(capulet_engine, spindler_battery, carrigan_tires)
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int, tire_values: list[float]) -> Glissade:
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        octoprime_tires = OctoprimeTire(tire_values)
        car = Glissade(willoughby_engine, spindler_battery, octoprime_tires)
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date,
                          warning_light_on: bool, tire_values: list[float]) -> Palindrome:
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        carrigan_tires = CarriganTire(tire_values)
        car = Palindrome(sternman_engine, spindler_battery, carrigan_tires)
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int, tire_values: list[float]) -> Rorschach:
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        octoprime_tires = OctoprimeTire(tire_values)
        car = Rorschach(willoughby_engine, nubbin_battery, octoprime_tires)
        return car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int, tire_values: list[float]) -> Thovex:
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        carrigan_tires = CarriganTire(tire_values)
        car = Thovex(capulet_engine, nubbin_battery, carrigan_tires)
        return car
