from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine


class Calliope(Car):
    def __init__(self, engine: CapuletEngine, battery: SpindlerBattery):
        super().__init__(engine, battery)
