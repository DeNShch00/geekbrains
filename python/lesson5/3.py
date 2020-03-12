"""
Создать текстовый файл (не программно),
 построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""


def main():
    employees = {}

    with open('file3.txt', encoding='utf-8') as file:
        for num, line in enumerate(file):
            try:
                name, salary = line.split()
            except ValueError:
                print(f'Line {num + 1}: bad format, must be: "<name> <salary>"')
                return

            try:
                employees[name] = float(salary)
            except ValueError:
                print(f'Line {num + 1}: <salary> must be a real number')
                return

    print('Employees with less than 20000 salary: ', [k for k, v in employees.items() if v < 20000])
    print(f'Average salary: {sum(employees.values())/len(employees):.2f}')


if __name__ == "__main__":
    main()
