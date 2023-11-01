from datetime import date

from .battery import Battery
from utils import add_years_to_date


class NubbinBattery(Battery):
    _last_service_date: date = None
    _current_date: date = None

    def __init__(self, last_service_date: date, current_date: date):
        self._last_service_date = last_service_date
        self._current_date = current_date

    def need_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self._last_service_date, 4)
        if date_which_battery_should_be_serviced_by < self._current_date:
            print("Your battery service is done!")
            return True
        print("Your battery is in good condition, No service required!")
        return False
