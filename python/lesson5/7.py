"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json


def main():
    companies = {}
    format_msg = 'Line {0}: bad format, must be: ' \
                 '"<company:str> <ownership:str> <income:int> <costs:int>"'

    with open('file7-1.txt', encoding='utf-8') as file:
        for num, line in enumerate(file):
            try:
                company, ownership, income, costs = line.split()
            except ValueError:
                print(format_msg.format(num + 1))
                return

            try:
                companies[company] = {'ownership': ownership, 'income': float(income), 'costs': float(costs)}
            except ValueError:
                print(format_msg.format(num + 1))
                return

    profit_by_company = {k: v['income'] - v['costs'] for k, v in companies.items()}
    profits = [v['income'] - v['costs'] for v in companies.values() if v['income'] > v['costs']]
    results = [profit_by_company, {'average_profit': sum(profits)/len(profits)}]

    with open('file7-2.json', 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
