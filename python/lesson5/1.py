"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('file1.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Input new string or empty string to done: ')
        if not line:
            break

        file.write(line + '\n')
