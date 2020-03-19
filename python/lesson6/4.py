"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car "{self.name}"({self.__class__.__name__}) GO')

    def stop(self):
        print(f'Car "{self.name}"({self.__class__.__name__}) STOP')

    def turn(self, direction):
        print(f'Car "{self.name}"({self.__class__.__name__}) TURN {direction}')

    def show_speed(self):
        print(f'Car "{self.name}"({self.__class__.__name__}) speed: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('speed limit exceeded!')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('speed limit exceeded!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(70, 'black', 'Audi')
sport_car = SportCar(100, 'red', 'Ferrari')
work_car = WorkCar(30, 'yellow', 'Caterpillar')
police_car = PoliceCar(90, 'white', 'Ford')

for obj in (town_car, sport_car, work_car, police_car):
    print(obj.name, obj.color, obj.speed, 'Police' if obj.is_police else '')
    obj.go()
    obj.stop()
    obj.turn('left')
    obj.show_speed()
