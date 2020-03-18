"""
практике работу декоратора @property.
Реализовать программу работы с органическими клетками, состоящими из ячеек. Н
еобходимо создать класс Клетка.
 его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
  сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
 умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
 если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
 как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
 как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, n):
        if not isinstance(n, int):
            raise TypeError(f"'Cell' must initialize with 'int', not '{type(n).__name__}'")
        elif n < 1:
            raise ValueError("'Cell' must initialize with positive value")

        self.n = n

    @staticmethod
    def _cell_type(obj):
        if not isinstance(obj, Cell):
            raise TypeError(f"can operate only with 'Cell', not '{type(obj).__name__}'")

    def __add__(self, other):
        self._cell_type(other)
        return Cell(self.n + other.n)

    def __sub__(self, other):
        self._cell_type(other)
        if self.n > other.n:
            return Cell(self.n - other.n)
        else:
            raise ValueError("left 'Cell' must be greater than right 'Cell'")

    def __mul__(self, other):
        self._cell_type(other)
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        self._cell_type(other)
        if self.n > other.n:
            return Cell(self.n // other.n)
        else:
            raise ValueError("left 'Cell' must be greater than right 'Cell'")

    def __eq__(self, other):
        self._cell_type(other)
        return self.n == other.n

    def make_order(self, per_line=0):
        if not per_line:
            return '*' * self.n

        count = self.n // per_line
        last = self.n % per_line
        return '\n'.join(['*' * per_line] * count + (['*' * last] if last else []))


assert Cell(5) + Cell(6) + Cell(7) == Cell(18)
assert Cell(10) - Cell(2) - Cell(2) - Cell(3) == Cell(3)
assert Cell(4) * Cell(4) * Cell(4) == Cell(64)
assert Cell(101) / Cell(10) == Cell(10)
c1 = Cell(12)
print(c1.make_order(5))
