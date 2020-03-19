"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
    Информатика:   100(л)   50(пр)   20(лаб)
    Физика:   30(л)   —   10(лаб)
    Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def main():
    subjects = {}
    format_msg = 'Line {0}: bad format, must be: ' \
                 '"<subject:str>: (<lectures_count:int>(l) | —) ' \
                 '(<practicals_count:int>(pr) | —)  ' \
                 '(<laboratories_count:int>(lab) | —)"'

    with open('file6.txt', encoding='utf-8') as file:
        for num, line in enumerate(file):
            try:
                subject, other = line.split(':', maxsplit=1)
            except ValueError:
                print(format_msg.format(num + 1))
                return

            subjects[subject] = 0

            try:
                lectures, practicals, laboratories = other.split()
            except ValueError:
                print(format_msg.format(num + 1))
                return

            for work in (lectures, practicals, laboratories):
                if work != '—':
                    try:
                        subjects[subject] += int(work.split('(')[0])
                    except (ValueError, IndexError):
                        print(format_msg.format(num + 1))
                        return

    print(subjects)


if __name__ == "__main__":
    main()
