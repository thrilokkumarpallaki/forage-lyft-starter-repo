from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, engine: SternmanEngine, battery: SpindlerBattery):
        super().__init__(engine, battery)
