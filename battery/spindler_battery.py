from datetime import date

from .battery import Battery


class SpindlerBattery(Battery):
    _last_service_date: date = None
    _current_date: date = None

    def __init__(self, current_date: date, last_service_date: date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def need_service(self):
        if (self._current_date - self._last_service_date).days >= 730:
            print("Your battery service is done!")
            return True
        print("Your battery is in good condition, No service required!")
        return False
