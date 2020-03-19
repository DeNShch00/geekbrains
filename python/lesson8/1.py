"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str):
        self.date = self.parse(date_str)
        self.validate_limits(*self.date)

    @classmethod
    def parse(cls, date_str):
        items = date_str.split('-')

        if len(items) != 3:
            raise ValueError('format must be DD-MM-YYYY where each component is natural number')

        return int(items[0]), int(items[1]), int(items[2])

    @staticmethod
    def validate_limits(day, month, year):
        # TODO: реализовать честную провекрку с учетом количества дней в разных месяцах, в том числе високосных

        if not 1 <= day <= 30:
            raise ValueError('day must be from 1 to 30')

        if not 1 <= month <= 12:
            raise ValueError('month must be from 1 to 12')

        if year < 0:
            raise ValueError('year must be positive number')

    def __str__(self):
        return str(self.date)


date = Date('11-10-1944')
print(date)
