"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random


def int_seq_file(file_name, seq_len, min_int=1, max_int=1000):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(seq_len):
            file.write(str(random.randint(min_int, max_int)))
            if i != seq_len - 1:
                file.write(' ')


def int_seq_sum(file_name):
    sum_ = 0
    prev_buff = ''
    with open(file_name, encoding='utf-8') as file:
        while True:
            portion = file.read(1024)
            buff = prev_buff + portion
            if not buff:
                break

            if not portion or buff[-1] == ' ':
                nums = buff.split()
                prev_buff = ''
            else:
                *nums, prev_buff = buff.split()

            sum_ += sum(map(int, nums))

    return sum_


def mem_int_seq_sum(file_name):
    with open(file_name, encoding='utf-8') as file:
        return sum(map(int, file.read().split()))


def main():
    file = 'file5.txt'
    int_seq_file(file, 100000)
    print('Sum: ', int_seq_sum(file))
    print('Sum (memory cost): ', mem_int_seq_sum(file))


if __name__ == "__main__":
    main()
