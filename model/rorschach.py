from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from tire.octoprime_tire import OctoprimeTire


class Rorschach(Car):
    def __init__(self, engine: WilloughbyEngine, battery: NubbinBattery, tire: OctoprimeTire):
        super().__init__(engine, battery, tire)
