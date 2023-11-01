import unittest
from datetime import datetime

from battery import NubbinBattery, SpindlerBattery
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 24_523
        current_mileage = 67_988
        car = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(car.need_service())

    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 30_000
        current_mileage = 45_000
        car = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(car.need_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_indicator_on = True
        engine = SternmanEngine(warning_indicator_on)
        self.assertTrue(engine.need_service())

    def test_engine_should_not_be_serviced(self):
        warning_indicator_on = False
        engine = SternmanEngine(warning_indicator_on)
        self.assertFalse(engine.need_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 7_523
        current_mileage = 70_988
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.need_service())

    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 45_000
        current_mileage = 65_000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.need_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = datetime.today().replace(year=2014).date()
        current_date = datetime.today().date()
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.need_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = datetime.today().replace(year=2023).date()
        current_date = datetime.today().date()
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.need_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = datetime.today().replace(year=2021).date()
        current_date = datetime.today().date()
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.need_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = datetime.today().replace(year=2022).date()
        current_date = datetime.today().date()
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.need_service())


if __name__ == '__main__':
    unittest.main()
