"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

items = [None, 1, 2.2, 'boo', True, (1, 2), [3, 4], {5, 6}, {'a': 1, 'b': 2}]
types = [type(None), int, float, str, bool, tuple, list, set, dict]
for i, t in zip(items, types):
    if type(i) is not t:
        print(f'TypeError: item {i} has type {type(i)}, expected {t}')
