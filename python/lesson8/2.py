"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
 и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, msg):
        self.msg = msg


def division(a, b):
    if b == 0:
        raise MyZeroDivisionError('division by zero')

    return a/b


def main():
    print('Count a/b')
    a = float(input('Input a: '))
    b = float(input('Input b: '))
    try:
        print('Result', division(a, b))
    except MyZeroDivisionError as e:
        print(e)


main()
