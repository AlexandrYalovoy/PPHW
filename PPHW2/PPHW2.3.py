# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

months_dict = {'1': 'Январь',
               '2': 'Февраль',
               '3': 'Март',
               '4': 'Апрель',
               '5': 'Май',
               '6': 'Июнь',
               '7': 'Июль',
               '8': 'Август',
               '9': 'Сентябрь',
               '10': 'Октябрь',
               '11': 'Ноябрь',
               '12': 'Декабрь'}

months_list = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
               'Ноябрь', 'Декабрь')
while True:
    users_month = input('Введите номер вашего месяца - ')

    if users_month.isdigit() and int(users_month) > 0 and int(users_month) < 13:
        if users_month == '12' or users_month == '1' or users_month == '2':
            seasons = 'Зима'
        elif users_month == '3' or users_month == '4' or users_month == '5':
            seasons = 'Весна'
        elif users_month == '6' or users_month == '7' or users_month == '8':
            seasons = 'Лето'
        else:
            seasons = 'Осень'

        break
    else:
        print('Вводите только цмфру тождественную месяцу, если "январь" то "1".')

print('\nМетод с использованием словаря - "dict".')
print(f'Введенная вами цифра соответсвует месяцу {months_dict[users_month]}, время года {seasons}.')

print('\nМетод с использованием списка - "list".')
print(f'Введенная вами цифра соответсвует месяцу {months_list[int(users_month) - 1]}, время года {seasons}.')
