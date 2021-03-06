"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
 пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. П
ри вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
 только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class NotIntNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg


def main():
    nums = []
    while True:
        s = input('Enter integer number of "stop" to done input: ')
        if s == 'stop':
            break

        try:
            error = True
            if len(s) > 0:
                if s.isdigit():
                    error = False
                elif s[0] == '-' and s[1:].isdigit():
                    error = False

            if error:
                raise NotIntNumberError('You input not an integer number')

            nums.append(int(s))
        except NotIntNumberError as e:
            print(e)

    print(nums)


main()
