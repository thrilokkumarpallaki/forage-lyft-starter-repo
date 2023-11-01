from datetime import datetime, date
from car_factory.car_factory import CarFactory

if __name__ == '__main__':
    last_service_date: date = datetime.today().replace(year=2012).date()
    current_date = datetime.today().date()

    last_service_mileage = 738023
    current_mileage = 987583

    tire_values = [0.4, 0.5, 0.6, 0.9]

    car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,
                                     tire_values)
    car.need_service()

    thovex_car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,
                                             tire_values)
    thovex_car.need_service()
