# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

max_number = 0

while True:
    numbers = input('Введи какое нибудь число типа "1234567" и я найду для тебя в нем самое большое чилсло -  ')
    if numbers.isdigit() == True:
        break
    else:
        print('Вводи тольцо цифры, я наблюдаю за тобой!!')

for number in numbers:
    if int(number) > max_number:
        max_number = int(number)

    if int(number) == 9:
        max_number = 9
        break

print(max_number)