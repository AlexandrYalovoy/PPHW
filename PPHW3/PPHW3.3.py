# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_two_max(arg_1, arg_2, arg_3):
    """
    Функция суммирует 2 числа выбирая наибольшие
    :param arg_1: Первый аргумент
    :param arg_2: Второй аргумент
    :param arg_3: Третий аргумент
    :return: возврашает сумму двух наибольших чисел
    """

    list_check = [arg_1, arg_2, arg_3]
    firs_arg = list_check.pop(list_check.index(max(list_check)))
    second_arg = list_check.pop(list_check.index(max(list_check)))
    return firs_arg + second_arg


sum_test = sum_two_max(4, 2, 3)

print(sum_test)

