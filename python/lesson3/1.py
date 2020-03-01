"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def ask_float(prompt):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print('Not a number. Try again')


def ask_divisor():
    while True:
        n = ask_float('Input divisor: ')
        if n == 0:
            print("Divisor can't be zero")
        else:
            return n


def ask_dividend():
    return ask_float('Input dividend: ')


def division(dividend, divisor):
    return dividend/divisor


def main():
    dividend = ask_dividend()
    divisor = ask_divisor()
    print(f'Result ({dividend} / {divisor}): {division(dividend, divisor)}')


main()
