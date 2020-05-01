# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import re
import time


class Date:
    def __init__(self, check=True, date_str_class_m=''):
        self.date_str = Date.check_format_date_str() if check else date_str_class_m
        self.date_list = self.transmutation_str_in_num()

    @staticmethod
    def check_format_date_str(auto=False):

        def check_real_date(check):
            try:
                date = time.strptime(check, '%d-%m-%Y')
            except ValueError:
                return False
            else:
                return True

        if auto:
            return '16-07-2020'
        while True:
            check = input('Введите дату в формате «дд-мм-гггг» - ')
            if re.search(r'[0-9]{2}[-][0-9]{2}[-][0-9]{4}$', check):
                if check_real_date(check):
                    return check
                else:
                    print('Введена несуществующая дата!!!')
                    continue
            else:
                print('Дата введена в неверном формате!!!')

    def transmutation_str_in_num(self):
        date_int_list = self.date_str.split('-')
        for i in range(0, 3):
            date_int_list[i] = int(date_int_list[i])
        return date_int_list

    @classmethod
    def transmutation_class(cls, date_str, check_on_off=False):
        return cls(check=check_on_off, date_str_class_m=date_str)


a = Date()
print('Вариант когда создается класс и спрашивает пользователя до тех пор пока не получит необходимое и корректное!')
print(a.date_str)

print(a.date_list)

print()
print('Вариант когда создается класс путем прямой передачи даты в класс без проверки. Я решил что метод класса '
      'должен что то менять, а обработка в цифры мне не нужна вовсе, но выполняется в обоих случаях для красоты. ')
b = Date.transmutation_class('16-07-2020')

print(b.date_str)

print(b.date_list)
