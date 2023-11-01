from car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire


class Thovex(Car):
    def __init__(self, engine: CapuletEngine, battery: NubbinBattery, tire: CarriganTire):
        super().__init__(engine, battery, tire)
