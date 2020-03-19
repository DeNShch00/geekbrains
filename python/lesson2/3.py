"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_list = ['winter']*2 + ['spring']*3 + ['summer']*3 + ['autumn']*3 + ['winter']
seasons_dict = {k: v for k, v in enumerate(seasons_list)}

while True:
    s = input('Enter month number (1-12): ')
    if s.isdigit():
        n = int(s)
        if 1 <= n <= 12:
            print(f'Season by list "{seasons_list[n-1]}", season by dict "{seasons_dict[n-1]}"')
            break
