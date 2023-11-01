from .engine import Engine
from datetime import date


class WilloughbyEngine(Engine):
    _last_service_mileage: int = 0
    _current_mileage: int = 0

    def __init__(self, last_service_mileage: int, current_mileage: int):
        self._last_service_mileage = last_service_mileage
        self._current_mileage = current_mileage

    def need_service(self):
        if self._current_mileage - self._last_service_mileage >= 60_000:
            print("Engine: Your engine is serviced!")
            return True

        print("Engine: Your engine is in good condition, No service is required!")
        return False
