# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, brand, is_police):
        self.speed = speed
        self.color = color
        self.brand = brand
        self.is_police = is_police

    def go(self):
        print('Автомобиль начал движение')

    def stop(self):
        print('Автомобиль закончил движение')

    def turn_right(self):
        print('Автомобиль повернул направо')

    def turn_left(self):
        print('Автомобиль повернул налево')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, brand, is_police, callsign, has_v_camera):
        super().__init__(speed, color, brand, is_police)
        self.callsign = callsign
        self.has_v_camera = has_v_camera

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышена максимально допустимая скорость. Не гони! Тебя ждут дома.')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышена максимально допустимая скорость. Необходимо замедлиться.')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')

class SportCar(Car):
    def show_speed(self):
        if self.speed < 120:
            print('Поддай газу, парень! Так ты никому ничего не докажешь!')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')

town_car_1 = TownCar(80, 'grey', 'BMW', False)
print(town_car_1.brand)
town_car_1.turn_right()
town_car_1.show_speed()

town_car_1 = TownCar(55, 'green', 'Kia', False)
town_car_1.show_speed()

work_car_1 = WorkCar(43, 'light yellow', 'Komatsu', False)
print(work_car_1.brand)
work_car_1.show_speed()

sport_car_1 = SportCar(100, 'red', 'Ferrari', False)
print(sport_car_1.brand, sport_car_1.color)
sport_car_1.show_speed()

police_car_1 = PoliceCar(60, 'black', 'Mercedes', True, 321, False)
print(police_car_1.is_police)
print(police_car_1.callsign, police_car_1.has_v_camera)
police_car_1.show_speed()

