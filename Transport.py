class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self):
        print('Бренд машины:', self.brand)
        print('Модель машины:', self.model)
        print('Год выпуска:', self.year)


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed

    def info(self):
        super().info()
        print('Тип топлива:', self.fuel_type)
        print('Максимальная скорость:', self.max_speed)
        print('Объём двигателя (см³):', self.engine_capacity)
        print('Угловая скорость (об/мин):', self.rotation_speed)
        
    def engine_power_calc(self):
        power = (self.engine_capacity * self.rotation_speed) / 9550
        return power



