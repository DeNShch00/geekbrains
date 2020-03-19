"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def print_user(*, name, surname, birthday, city, email, phone):
    print(f'User: {name}, {surname}, {birthday}, {city}, {email}, {phone}')


print_user(name='Keanu', surname='Reeves', birthday='02.09.1964', city='New York',
           email='reeves@google.com', phone='0-000-00-00-0')
