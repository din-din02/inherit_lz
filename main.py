from Transport import Car


def main():
    print('Введите данные машины:')
    brand = input("Бренд: ")
    model = input("Модель: ")
    year = int(input("Год выпуска: "))
    fuel_type = input("Тип топлива: ")
    max_speed = int(input("Максимальная скорость (км/ч): "))
    engine_capacity = float(input("Объём двигателя (см³): "))
    rotation_speed = float(input("Угловая скорость (об/мин): "))
    print('*'*30)
    car = Car(brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed)
    car.info()
    P= car.engine_power_calc()
    print('Мощность двигателя (кВт):',P)
if __name__ == '__main__':
    main()