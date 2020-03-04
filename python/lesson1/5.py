"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).

Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""


def ask_int(prompt):
    s = ''
    while not s.isdigit():
        s = input(prompt)

    return int(s)


income = ask_int('Enter income: ')
costs = ask_int('Enter costs: ')
if income > costs:
    profit = income - costs
    print(f'Your company has profit: {profit}, margin: {profit/income:.2%}')
    employees = ask_int('Enter employees count: ')
    print(f'profit per employee: {profit/employees:.2f}')
elif income == costs:
    print(f'Your company has zero profit')
else:
    print(f'Your company has lesion: {costs - income}')
