"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
"""

in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
out_list = [in_list[i] for i in range(1, len(in_list)) if in_list[i] > in_list[i-1]]
print(out_list)