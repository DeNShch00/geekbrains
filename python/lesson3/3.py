"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def max2_sum(n1, n2, n3):
    return n1 + n2 + n3 - min(n1, n2, n3)


print(f'max2_sum(1, 2, 3) = {max2_sum(1, 2, 3)}')
print(f'max2_sum(3, 2, 1) = {max2_sum(3, 2, 1)}')
print(f'max2_sum(1, 3, 2) = {max2_sum(1, 3, 2)}')
print(f'max2_sum(2, 2, 2) = {max2_sum(2, 2, 2)}')
