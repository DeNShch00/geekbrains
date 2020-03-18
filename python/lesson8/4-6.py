"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
 можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
 изученных на уроках по ООП.
"""

from abc import ABC
from collections import Counter


class DeviceStore:
    departments = ('Store', 'Logistics', 'Production', 'Sales')

    def __init__(self):
        self.devices = {}

    def add(self, device):
        """
            Добавление новой техники на склад
        """
        if not isinstance(device, Device):
            raise TypeError('device object must be derived from Device class')
        if device in self.devices:
            raise ValueError('device already in DeviceStore')

        self.devices[device] = 'Store'

    def give(self, devices, department):
        """
            Выдача техники со склада в отдел
        """
        if department not in self.departments:
            raise ValueError(f'department must be in {self.departments}')

    def back(self, devices):
        """
            Возвращение техники на склад
        """
        pass

    def filter(self, **kwargs):
        """
            Список техники с определенными атрибутами
        """
        result = []

        for one in self.devices:
            match = (1 for key, value in kwargs if key in one.__dict__ and one.__dict__[key] == value)
            if sum(match) == len(kwargs):
                result.append(one)

        return result

    def count(self):
        """
            Общее количество техники каждого типа
        """
        return Counter(one.__class__.__name__ for one in self.devices).items()


class Device(ABC):
    def __init__(self, model, vendor, serial_num, price):
        self.model = model
        self.vendor = vendor
        self.serial_num = serial_num
        self.price = price

    def __str__(self):
        return f'{self.__class__.__name__} S/N "{self.serial_num}": model="{self.model}" vendor="{self.vendor}" ' \
            f'price="{self.price}$"'


class Printer(Device):
    def __init__(self, model, vendor, serial_num, price, print_type, is_color):
        super().__init__(model, vendor, serial_num, price)
        self.print_type = print_type
        self.is_color = is_color

    def __str__(self):
        return super().__str__() + f' print_type="{self.print_type}" is_color="{self.is_color}"'


class Scanner(Device):
    def __init__(self, model, vendor, serial_num, price, dpi):
        super().__init__(model, vendor, serial_num, price)
        self.dpi = dpi

    def __str__(self):
        return super().__str__() + f' dpi="{self.dpi}"'


p = Printer('LJ234', 'HP', '4324DW432', 344.3, 'LaserJet', False)
p2 = Printer('CN23E', 'Cannon', 'QW-4454R34', 155.2, 'BubbleJet', True)
print(p)
f = {p:5}
if p in f:
    print('dd')

dc = DeviceStore()

dc.add(p)
dc.add(p2)
print(dc.count())