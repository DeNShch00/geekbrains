"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

s = ''
while not s.isdigit():
    s = input('Enter a number: ')

n = int(s)
max_digit = 0
while n:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit

    n = n // 10

print(f'max digit in {s} is {max_digit}')
