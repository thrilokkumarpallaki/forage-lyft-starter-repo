from datetime import datetime, date
from car_factory.car_factory import CarFactory

if __name__ == '__main__':
    last_service_date: date = datetime.today().replace(year=2021).date()
    current_date = datetime.today().date()

    last_service_mileage = 738023
    current_mileage = 987583

    car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    car.need_service()

    thovex_car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
    thovex_car.need_service()
