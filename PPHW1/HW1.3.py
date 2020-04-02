# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

while True:
    number_str = input('Введите целое число для суммирования по принципе "3 + 33 + 333 = 369" -  ')

    if number_str.isdigit() == True:
        result = int(number_str) + int(number_str * 2) + int(number_str * 3)
        print(result)
        break
    else:
        print('Вводи тольцо цифры, я наблюдаю за тобой!!')
