from datetime import date

from .battery import Battery


class NubbinBattery(Battery):
    _last_service_date: date = None
    _current_date: date = None

    def __init__(self, last_service_date: date, current_date: date):
        self._last_service_date = last_service_date
        self._current_date = current_date

    def need_service(self):
        if (self._current_date - self._last_service_date).days >= 1460:
            print("Your battery service is done!")
            return True
        print("Your battery is in good condition, No service required!")
        return False
