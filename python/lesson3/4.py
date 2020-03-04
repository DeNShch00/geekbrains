"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def pow_std(x, y):
    return x ** y


def pow_cycle(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return 1

    n = 1
    for i in range(abs(y)):
        n *= x

    if y < 0:
        return 1/n

    return n


def ask_positive_number(prompt, number_type):
    while True:
        s = input(prompt)
        try:
            n = number_type(s)
        except ValueError:
            print('Incorrect number literal')
            continue

        if n <= 0:
            print('Number must be positive')
        else:
            return n


def ask_positive_int(prompt):
    return ask_positive_number(prompt, int)


def ask_positive_float(prompt):
    return ask_positive_number(prompt, float)


def main():
    print('Count: x ** (-y); x - positive real number, y - positive natural number')
    x = ask_positive_float('Input x: ')
    y = ask_positive_int('Input y: ')
    print(f'Result {x} ** (-{y}): pow_std={pow_std(x, -y)}, pow_cycle={pow_cycle(x, -y)}')


main()
