from abc import ABC
from battery.battery import Battery
from engine.engine import Engine
from tire.tire import Tire

from serviceable import Serviceable


class Car(Serviceable, ABC):
    engine: Engine = None
    battery: Battery = None
    tires: Tire = None

    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def need_service(self):
        self.engine.need_service()
        self.battery.need_service()
        self.tire.need_service()
