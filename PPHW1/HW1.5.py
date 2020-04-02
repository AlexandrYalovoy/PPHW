# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

def float_numbers_check(text_question):
    while True:
        check = input(text_question)
        if check.isdigit():
            return float(check)
        else:
            print('Вводи тольцо цифры, я наблюдаю за тобой!!')

currency = float_numbers_check('Выберите валюту: \n'
                               '1 - Рубли (\u20bd);\n'
                               '2 - Доллары (\u0024);\n'
                               '3 - Евро (\u20ac);\n'
                               '4 - Юани (\u5143);\n'
                               '5 - иная валюта.\n'
                               'Введите номер выбраной валюты -  ')

if currency == 1:
    currency = '\u20bd'
elif currency == 2:
    currency = '\u0024'
elif currency == 3:
    currency = '\u20ac'
elif currency == 4:
    currency = '\u5143'
else:
    currency = ''

revenue = float_numbers_check(f'\nВведите выручку фирмы в {currency} -  ')

costs = float_numbers_check(f'Введите издержки фирмы в {currency} -  ')

result_cash = revenue - costs

if revenue < costs:
    print(f'\nВаша фирма убыточна, понесенные убытки {abs(result_cash)} {currency}')
elif revenue == costs:
    print('\nВаша фирма не приносит прибыли')
else:
    print(f'\nПрибыль составила - {result_cash} {currency}')
    print(f'Рентабильность составила {round((result_cash / revenue), 2)}')
    staff = float_numbers_check('Введите количество сотрудников - ')
    print(f'Прибыль на сотрудника составила - {result_cash / staff} {currency}')


