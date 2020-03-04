"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

s = ''
while not s.isdigit():
    s = input('Enter time in seconds: ')

time_seconds = int(s)
hours = time_seconds // 3600
minutes = (time_seconds % 3600) // 60
seconds = time_seconds % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')
