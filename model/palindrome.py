from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire


class Palindrome(Car):
    def __init__(self, engine: SternmanEngine, battery: SpindlerBattery, tire: CarriganTire):
        super().__init__(engine, battery, tire)
