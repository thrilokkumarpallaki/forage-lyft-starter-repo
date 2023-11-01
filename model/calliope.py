from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from tire.carrigan_tire import CarriganTire


class Calliope(Car):
    def __init__(self, engine: CapuletEngine, battery: SpindlerBattery, tire: CarriganTire):
        super().__init__(engine, battery, tire)
