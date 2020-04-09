# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_num_str():  # Функция суммирования цифр строк
    """
    Функция суммирования цифр из строк содержаших все на свете, и делающей стоп по символу "!".
    Хранит в соответствующих переменных данные о том какие вообще цифры содержались в строках, какие символы
    содержались в строках, сами строки от каждого ввода.
    Ничего не возвращает принтует только сумму цифр по логике сумма вводаов плюс сумма последующего ввода
    result_summ += sum(work_list)

    :param result_summ: Глобальная переменная результата суммирования всех вводов.
           Храннит в себе сумму чиселл всех вводов.
           hub_numbers_sum: Глобальная переменная в которой храниться список всех введенных чисел;
           hub_users_str: Глобальная переменная в которой храниться список всех введенных строк;
           hub_users_symbols: Глобальная переменная в которой храниться список всех введенных символов в кортеже;
           stop_symbol: Переменная стоп символа, обнуляется при каждом вызове функции;
           work_list: Рабочий список хаб, создается новый при каждом проходе цикла while, содержит только цифры этого
           ввода;
    :return: Ничего не возвращает только принтует result_summ
    """

    # Глобальные запихал для того чтоб максимум из методички был тут.
    global result_summ
    global hub_numbers_sum
    global hub_users_str
    global hub_users_symbols
    stop_symbol = None

    while True:

        users_str = input('Введите строку чисел разделенную пробелами. Стоп символ "!" - ')

        hub_users_str.append(users_str)

        users_str = users_str.split()

        hub_users_symbols.append(tuple(users_str))

        work_list = []

        for i in users_str:
            check = check_numbers_float(i)
            if check == '!':
                stop_symbol = '!'
                break
            elif check != None:
                work_list.append(check)

        if work_list != []:
            hub_numbers_sum.extend(work_list)

        if hub_numbers_sum == []:
            print('Ни одного числа небыло введено')
        else:
            result_summ += sum(work_list)
            print(result_summ)

        # print(result_summ)

        if stop_symbol == '!':
            break


def check_numbers_float(arg_1):  # Функция возврашает либо float(число) либо '!'
    """
    Функция проверяет действительное ли это число float или стоп символ "!".
    В противном случае ничего не возвращает.

    :param arg_1: Число пользователя в фортмате str
    :return: возврашает либо float(число) либо '!'
    """
    try:
        number = float(arg_1)
    except ValueError:
        if arg_1 == '!':
            return arg_1
    else:
        return number


result_summ = 0  # Глобальная переменная результата суммирования всех вводов

hub_numbers_sum = []  # Глобальная переменная в которой храниться список всех введенных чисел

hub_users_str = []  # Глобальная переменная в которой храниться список всех введенных строк

hub_users_symbols = []  # Глобальная переменная в которой храниться список всех введенных символов в кортеже

sum_num_str()
