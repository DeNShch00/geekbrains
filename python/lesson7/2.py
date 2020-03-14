"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
 для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
 проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def cloth_count(self):
        pass


class Coat(Clothes):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    @property
    def cloth_count(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height

    @property
    def cloth_count(self):
        return 2 * self.height + 0.3


coat = Coat('Armani', 65)
suit = Suit('Gucci', 10)
print(f'Cloth count for coat "{coat.title}"/{coat.size} and suit "{suit.title}"/{suit.height}:',
      coat.cloth_count + suit.cloth_count)
