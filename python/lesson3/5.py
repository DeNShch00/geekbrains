"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
 к полученной ранее сумме и после этого завершить программу.
"""


def sum_seq():
    cur_sum = 0
    is_done = False
    while True:
        s = input('Enter numbers separated by space or "q" to done input: ')
        for i in s.split():
            if i == "q":
                is_done = True
                break

            try:
                i = float(i)
            except ValueError:
                print(f'"{i}" was excluded, it\'s not a number')
                continue

            cur_sum += i

        print('Current sum: ', cur_sum)
        if is_done:
            break


sum_seq()
