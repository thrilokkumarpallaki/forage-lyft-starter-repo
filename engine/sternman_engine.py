from .engine import Engine
from datetime import date


class SternmanEngine(Engine):
    _is_warning_indicator_on: bool = False

    def __init__(self, is_warning_indicator_on: bool):
        self._is_warning_indicator_on = is_warning_indicator_on

    def need_service(self) -> bool:
        if self._is_warning_indicator_on:
            print("Engine: Your engine is serviced!")
            return True

        print("Engine: Your engine is in good condition, No service is required!")
        return False
