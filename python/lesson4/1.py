"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys


def get_arg(pos, type_, pos_err_msg, type_err_msg):
    try:
        return type_(sys.argv[pos])
    except IndexError:
        print(pos_err_msg)
        exit(1)
    except ValueError:
        print(type_err_msg)
        exit(1)


def main():
    few_args = 'Invalid args count, usage: python.exe 1.py <hours> <tariff> <bounty>'
    hours = get_arg(1, float, few_args, '<hours> must be real number')
    tariff = get_arg(2, float, few_args, '<tariff> must be real number')
    bounty = get_arg(3, float, few_args, '<bounty> must be real number')
    print('Salary: ', hours*tariff + bounty)


if __name__ == '__main__':
    main()
