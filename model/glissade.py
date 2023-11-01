from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery


class Glissade(Car):
    def __init__(self, engine: WilloughbyEngine, battery: SpindlerBattery):
        super().__init__(engine, battery)

