"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
 name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
 проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos1 = Position('Иван', 'Иванов', 'грузчик', 1000, 100)
pos2 = Position('Петр', 'Петров', 'водитель', 2200, 200)
pos3 = Position('Сидр', 'Сидоров', 'начальник', 3200, 300)

for obj in (pos1, pos2, pos3):
    print('name:', obj.name, 'surname:', obj.surname, 'position:', obj.position)
    print('full name:', obj.get_full_name())
    print('total income:', obj.get_total_income())
