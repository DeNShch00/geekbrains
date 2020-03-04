"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

items = []
while True:
    s = input(f'Enter list element {len(items)} or empty string to done editing: ')
    if not s:
        break

    items.append(s)

i = 0
limit = len(items) - 1
while i < limit:
    x = items[i]
    items[i] = items[i + 1]
    items[i + 1] = x
    i += 2

print('Result list: ', items)
