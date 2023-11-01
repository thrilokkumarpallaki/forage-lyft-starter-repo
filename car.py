from abc import ABC
from battery.battery import Battery
from engine.engine import Engine

from serviceable import Serviceable


class Car(Serviceable, ABC):
    engine: Engine = None
    battery: Battery = None

    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def need_service(self):
        self.engine.need_service()
        self.battery.need_service()
