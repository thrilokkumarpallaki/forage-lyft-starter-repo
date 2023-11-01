from .tire import Tire


class CarriganTire(Tire):
    _tire_values: list[float] = []

    def __init__(self, tire_values: list[float]):
        self._tire_values = tire_values

    def need_service(self):
        for tire_value in self._tire_values:
            if tire_value >= 0.9:
                print("Your tire service is done!")
                return True
        print("Your tires are in good condition, No service is required!")
        return False
