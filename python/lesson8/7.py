"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
 и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, re, im):
        if not isinstance(re, (int, float)) or not isinstance(im, (int, float)):
            raise TypeError('expected type "int" or "float" for re and im')

        self.re = re
        self.im = im

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError('expected type "ComplexNumber" for second operand')

        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError('expected type "ComplexNumber" for second operand')

        return ComplexNumber(self.re*other.re - self.im*other.im,
                             self.im*other.re + self.re*other.im)

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.re == other.re and self.im == other.im
        elif isinstance(other, complex):
            return self.re == other.real and self.im == other.imag
        else:
            raise TypeError('expected type "ComplexNumber" or "complex" for second operand')


assert ComplexNumber(2, 3) == complex(2, 3)
assert ComplexNumber(4, 5) + ComplexNumber(6, 7) == ComplexNumber(10, 12)
assert ComplexNumber(4, 5) + ComplexNumber(6, 7) == complex(4, 5) + complex(6, 7)
assert ComplexNumber(3, 8) * ComplexNumber(16, -4) == complex(3, 8) * complex(16, -4)
