"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
 для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
 складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    class InvalidMatrix(Exception):
        pass

    class NotEqualMatrixSize(Exception):
        pass

    def __init__(self, list_of_lists):
        self.matrix = list_of_lists
        self._validate()

    def _validate(self):
        container_types = list, tuple
        value_types = int, float

        if not isinstance(self.matrix, container_types) or len(self.matrix) < 1:
            raise self.InvalidMatrix

        row_size = 0
        if isinstance(self.matrix[0], container_types):
            row_size = len(self.matrix[0])

        if not row_size:
            raise self.InvalidMatrix

        for row in self.matrix:
            if not isinstance(row, container_types) or len(row) != row_size:
                raise self.InvalidMatrix

            for item in row:
                if not isinstance(item, value_types):
                    raise self.InvalidMatrix

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __str__(self):
        col_widths = []
        for col in range(len(self.matrix[0])):
            col_widths.append(max(len(str(row[col])) for row in self.matrix))

        str_matrix = ''
        str_item = '{{0:{0}}}'
        for row in self.matrix:
            str_row = ' '.join(str_item.format(col_widths[num]).format(item) for num, item in enumerate(row))
            str_matrix += '⃒ ' + str_row + ' ⃒\n'

        return str_matrix

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"can only add 'Matrix', not '{type(other).__name__}'")

        if self.size() != other.size():
            raise self.NotEqualMatrixSize

        result = []
        for row_l, row_r in zip(self.matrix, other.matrix):
            result_row = []
            for item_l, item_r in zip(row_l, row_r):
                result_row.append(item_l + item_r)

            result.append(result_row)

        return Matrix(result)


m1 = Matrix([[1, -2000, 4], [3, 40, 44], [5, 6, 10000]])
print(m1)
m2 = Matrix([[1, -2000, 4], [3, 40, 44], [5, 6, 10000]])
print(m2)
m3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(m3)

m4 = m1 + m2 + m3
print(m4)
