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


class DeviceStore:
    departments = ('Store', 'Logistics', 'Production', 'Sales')

    def __init__(self):
        self.devices = {}

    def add(self, device):
        """
            Добавление новой техники на склад
        """
        if not isinstance(device, Device):
            raise TypeError('device object must be derived from "Device" class')
        if device in self.devices:
            raise ValueError('device already in "DeviceStore"')

        self.devices[device] = 'Store'

    def give(self, devices, department):
        """
            Выдача техники со склада в отдел
        """
        if not isinstance(devices, (list, tuple)):
            raise TypeError('device must be "list" or "tuple"')

        if department not in self.departments:
            raise ValueError(f'department must be in {self.departments}')

        for dev in devices:
            if isinstance(dev, Device):
                try:
                    if self.devices[dev] == 'Store':
                        self.devices[dev] = department
                except KeyError:
                    pass

    def back(self, devices):
        """
            Возвращение техники на склад
        """
        if not isinstance(devices, (list, tuple)):
            raise TypeError('device must be "list" or "tuple"')

        for dev in devices:
            if isinstance(dev, Device):
                try:
                    self.devices[dev] = 'Store'
                except KeyError:
                    pass

    def filter(self, **kwargs):
        """
            Список техники с определенными атрибутами
        """
        result = []
        for one in self.devices:
            match = (1 for key, value in kwargs.items() if key in one.__dict__ and one.__dict__[key] == value)
            if sum(match) == len(kwargs):
                result.append(one)

        return result

    def report(self):
        """
            Отчет - наличие техники по отделам
        """
        result = ''
        types = {one.__class__.__name__ for one in self.devices}
        for dept in self.departments:
            result += dept + '\n'
            for type_ in sorted(types):
                count = 0
                dev_list = ''
                for dev, dev_dept in self.devices.items():
                    if type_ == dev.__class__.__name__ and dept == dev_dept:
                        dev_list += '\t\t' + str(dev) + '\n'
                        count += 1

                if count:
                    result += f'\t{type_}[{count}]:\n'
                    result += dev_list

        return result


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


dc = DeviceStore()
dc.add(Printer('LJ234', 'HP', '4324DW432', 344.3, 'LaserJet', False))
dc.add(Printer('BJ1134T', 'HP', 'THU34857', 564, 'BubbleJet', True))
dc.add(Printer('BJ1134TX', 'HP', 'REW4343', 567, 'BubbleJet', True))
dc.add(Printer('CN23E', 'Canon', 'QW-4454R34', 155.2, 'BubbleJet', True))
dc.add(Printer('CN23E', 'Canon', 'QW-3545456', 155.2, 'BubbleJet', True))
dc.add(Printer('E3434-G', 'Epson', 'E-33434-R4', 344.97, 'BubbleJet', True))
dc.add(Scanner('43FE', 'Canon', '5849GHJE', 188.55, 400))
dc.add(Scanner('R434', 'Epson', 'GHE457545', 1120, 800))
dc.add(Scanner('R434', 'Epson', 'T-57489754', 477, 800))
dc.add(Scanner('34FG', 'Canon', '47584FEH', 2300.7, 1200))
dc.add(Scanner('789U', 'Epson', '4-659865GJRE', 3456.99, 3200))
print(dc.report())
# Передать в отдел Логистики все струйные принтеры HP
dc.give(dc.filter(vendor='HP', print_type='BubbleJet'), 'Logistics')
# Передать в Продуктовый отдел все устройства модели 'CN23E'
dc.give(dc.filter(model='CN23E'), 'Production')
# Передать в Продуктовый все сканеры с разрешением 800dpi
dc.give(dc.filter(dpi=800), 'Production')
# Передать в отдел Продаж устройство с серийным номером '4-659865GJRE'
dc.give(dc.filter(serial_num='4-659865GJRE'), 'Sales')
print(dc.report())
# Вернуть на Склад устройство с серийным номером 'QW-3545456'
dc.back(dc.filter(serial_num='QW-3545456'))
print(dc.report())
