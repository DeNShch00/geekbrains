"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена должен составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""


def ask_int(prompt):
    s = ''
    while not s.isdigit():
        s = input(prompt)

    return int(s)


initial = ask_int('Enter initial result (km): ')
target = ask_int('Enter target result (km): ')
if initial > target:
    print('invalid input: initial is greater than target')
else:
    days = 1
    if initial != target:
        while True:
            days += 1
            initial += initial * 0.1
            if initial >= target:
                break

    print(f'days to reach the target: {days}')
