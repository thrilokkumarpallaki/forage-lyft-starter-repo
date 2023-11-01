from .tire import Tire


class OctoprimeTire(Tire):
    _tire_values: list[float] = []

    def __init__(self, tire_values: list[float]):
        self._tire_values = tire_values

    def need_service(self):
        all_tire_sum = sum(self._tire_values)
        if all_tire_sum >= 3.0:
            return True
        return False
