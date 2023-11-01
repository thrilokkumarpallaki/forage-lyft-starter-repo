from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from tire.octoprime_tire import OctoprimeTire


class Glissade(Car):
    def __init__(self, engine: WilloughbyEngine, battery: SpindlerBattery, tire: OctoprimeTire):
        super().__init__(engine, battery, tire)

