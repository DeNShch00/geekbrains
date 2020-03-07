"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
*объединить их
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
"""

from itertools import count, cycle


def main():
    # variant 1
    print('Variant 1')
    count_it = count()
    cycle_it = cycle('ABCD')
    for i in range(10):
        print(f'{i}: count->{next(count_it)}, cycle->{next(cycle_it)}')

    # variant 2
    print('Variant 2')
    for num, char in zip(count(), cycle('ABCD')):
        print(f'count->{num}, cycle->{char}')
        if num == 9:
            break


if __name__ == '__main__':
    main()
